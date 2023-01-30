import itertools

import mock 
import urllib.error
import pytest

import face.download as download

def test_get_asset_size():

      mock_url_opener = mock.mock_open()

      context = mock_url_opener.return_value.__enter__.return_value
      context.info = mock.Mock(return_value={"Content-Length": 10})

      kwargs = {"url_opener": mock_url_opener}
      size = download.get_asset_size(url="url", **kwargs)
      assert size == 10

class TestDownload:

      def setup(self, configuration):

            self.mock_url_opener = mock.mock_open()
            self.mock_url_context = self.mock_url_opener.return_value.__enter__.return_value

            self.mock_file_opener = mock.mock_open()
            self.mock_file_context = self.mock_file_opener.return_value.__enter__.return_value

            self.mock_url_request = mock.Mock()

            self.kwargs = {
                  "url_opener": self.mock_url_opener, 
                  "url_request": self.mock_url_request, 
                  "file_opener": self.mock_file_opener
            }

      def test_simple_one_read_download(self):

            self.mock_url_context.info = mock.Mock(return_value={"Content-Length": 10})

            # Data return by context 
            packet = 10 * [1]
            self.mock_url_context.read.side_effect = [packet, []]

            downloader = download.DatasetDownloader(url="whatever", path="whatever", **self.kwargs)

            downloader.download(verbose=False)

            assert 2 == self.mock_url_opener.call_count
            assert 1 == self.mock_url_request.call_count
            assert 1 == self.mock_file_opener.call_count

            self.mock_file_context.assert_called_once_with(packet)

            assert 10 == downloader.download_size_in_bytes

      def test_simple_download_over_multiple_callers(self):

            self.mock_url_context.info = mock.Mock(return_value={"Content-Length": 30})

            # Data return by context
            packet = 10 * [1]
            self.mock_url_context.read.side_effect = [packet, packet, packet, []]

            downloader = download.DatasetDownloader(url="whatever", path="whatever", **self.kwargs)

            downloader.download(verbose=False)

            assert 2 == self.mock_url_opener.call_count
            assert 1 == self.mock_url_request.call_count
            assert 1 == self.mock_file_opener.call_count

            calls = itertools.repeat(mock.call(packet), 3)
            self.mock_file_context.assert_has_calls(calls)
            assert 3 == self.mock_file_context.write.call_count

            assert 30 == downloader.download_size_in_bytes

      def test_download_with_error(self):

            self.mock_url_context.info = mock.Mock(return_value={"Content-Length": 30})

            # Data return by context
            packet = 10 * [1]
            self.mock_url_context.read.side_effect = [packet, TimeoutError(), packet, packet, []]

            downloader = download.DatasetDownloader(url="whatever", path="whatever", **self.kwargs)

            downloader.download(verbose=False)

            assert 3 == self.mock_url_opener.call_count
            assert 2 == self.mock_url_request.call_count
            assert 2 == self.mock_file_opener.call_count

            calls = itertools.repeat(mock.call(packet), 3)
            self.mock_file_context.assert_has_calls(calls)
            assert 3 == self.mock_file_context.write.call_count

            assert 30 == downloader.download_size_in_bytes

      def test_download_with_max_retries(self):

            self.mock_url_context.info = mock.Mock(return_value={"Content-Length": 30})

            # Data return by context
            packet = 10 * [1]
            self.mock_url_context.read.side_effect = [packet, TimeoutError(), TimeoutError(), packet, TimeoutError(), TimeoutError(), packet, []]

            downloader = download.DatasetDownloader(url="whatever", path="whatever", max_retries=3, **self.kwargs)

            with pytest.raises(TimeoutError):
                  downloader.download(verbose=False)

            assert 5 == self.mock_url_opener.call_count
            assert 4 == self.mock_url_request.call_count
            assert 4 == self.mock_file_opener.call_count

            calls = itertools.repeat(mock.call(packet), 2)
            self.mock_file_context.assert_has_calls(calls)
            assert 2 == self.mock_file_context.write.call_count

      def test_nothing_returned_before_download(self):

            self.mock_url_context.info = mock.Mock(return_value={"Content-Length": 30})

            # Data return by context
            packet = 10 * [1]
            self.mock_url_context.read.side_effect = [packet, packet, [], packet, packet, []]

            downloader = download.DatasetDownloader(url="whatever", path="whatever", **self.kwargs)

            downloader.download(verbose=False)

            assert 3 == self.mock_url_opener.call_count
            assert 2 == self.mock_url_request.call_count
            assert 2 == self.mock_file_opener.call_count

            calls = itertools.repeat(mock.call(packet), 4)
            self.mock_file_context.assert_has_calls(calls)
            assert 4 == self.mock_file_context.write.call_count

            assert 40 == downloader.download_size_in_bytes

            assert 1 == downloader.retry_count

      def test_download_resumed_after_too_short(self):

            self.mock_url_context.info = mock.Mock(return_value={"Content-Length": 40})

            # Data return by context
            packet = 10 * [1]
            connection_error = urllib.error.ContentTooShortError(message="Testing connection exception", content=[])
            self.mock_url_context.read.side_effect = [packet, packet, connection_error, packet, packet, []]

            downloader = download.DatasetDownloader(url="whatever", path="whatever", **self.kwargs)

            downloader.download(verbose=False)

            assert 3 == self.mock_url_opener.call_count
            assert 2 == self.mock_url_request.call_count
            assert 2 == self.mock_file_opener.call_count

            calls = itertools.repeat(mock.call(packet), 4)
            self.mock_file_context.assert_has_calls(calls)
            assert 4 == self.mock_file_context.write.call_count

            assert 40 == downloader.download_size_in_bytes
            assert 1 == downloader.retry_count

      def test_content_too_short_after_max_retries(self):

            self.mock_url_context.info = mock.Mock(return_value={"Content-Length": 40})

            # Data return by context
            packet = 10 * [1]
            connection_error = urllib.error.ContentTooShortError(message="Testing connection exception", content=[])
            self.mock_url_context.read.side_effect = [connection_error, packet, connection_error, connection_error, packet]

            downloader = download.DatasetDownloader(url="whatever", path="whatever", max_retries=2, **self.kwargs)

            with pytest.raises(urllib.error.ContentTooShortError):
                  downloader.download(verbose=False)

            assert 4 == self.mock_url_opener.call_count
            assert 3 == self.mock_url_request.call_count
            assert 3 == self.mock_file_opener.call_count

            self.mock_file_context.assert_once_called_with(packet)
            assert 1 == self.mock_file_context.write.call_count

            assert 10 == downloader.download_size_in_bytes
            assert 2 == downloader.retry_count
import urllib.request
import urllib.error

import tqdm

def get_asset_size(url, **kwargs):
      # Get size of asset

      url_opener = kwargs["url_opener"] if "url_opener" in kwargs else urllib.request.urlopen

      with url_opener(url) as url_connection:

            metadata = url_connection.info()
            return int(metadata["Content-Length"])

class DatasetDownloader:
      # Downloads datasets from the internet

      def __init__(self, url, path, max_retries=10, **kwargs):

            self.url = url
            self.path = path
            self.max_retries = max_retries

            self.url_opener = kwargs["url_opener"] if "url_opener" in kwargs else urllib.request.urlopen
            self.url_request = kwargs["url_request"] if "url_request" in kwargs else urllib.request.Request
            self.file_opener = kwargs["file_opener"] if "file_opener" in kwargs else open

            self.retry_count = 0
            self.download_size_in_bytes = 0

            self.total = get_asset_size(self.url, **kwargs)

            self.bytes_per_read = 8192  # 8 KB

      def download(self, verbose=True):
            # Download the dataset

            if verbose:
                  print("Downloading dataset from {} to {}".format(self.url))

            try:
                  request = self._get_request()
                  flags == "wb" if self.download_size_in_bytes is 0 else "ab"
                  
                  with self.url_opener(request) as url_connection, self.file_opener(self.path, flags) as file, \
                              tqdm.tqdm(total=self.total, disable=not verbose) as progress_bar:
                  
                        progress_bar.update(self.download_size_in_bytes)
                        data = url_connection.read(self.bytes_per_read)
                        
                        while len(data) != 0:

                              file.write(data)
                              self.download_size_in_bytes += len(data)

                              progress_bar.update(len(data))
                              data = url_connection.read(self.bytes_per_read)

                        if self.download_size_in_bytes != self.total:
                              raise urllib.error.ContentTooShortError(message="Downloaded size does not match expected size", content=data)

            except (TimeoutError, urllib.error.ContentTooShortError) as error:
                  self._handle_error(error)

      def _get_request(self):
            # Get the request object

            header = {"Range": 'bytes={}-{}'.format(self.download_size_in_bytes, self.total)}
            request = self.url_request(url=self.url, headers=header)

      def _handle_error(self, error, verbose):
            # Handle error

            if self.retry_count < self.max_retries:
                  if verbose:
                        print("Error downloading dataset. Retrying...")
            else:
                  if verbose:
                        print("Error downloading dataset. Maximum retries exceeded out of {} times. Aborting...".format(self.retry_count))
                  raise error
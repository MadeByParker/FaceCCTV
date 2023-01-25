from ..facecctv_ai import config
from ..facecctv_ai import data
def main():
      # Load data
      data.DatasetBuilder(config.dataset_path).build_dataset()

if __name__ == "__main__":
      main()
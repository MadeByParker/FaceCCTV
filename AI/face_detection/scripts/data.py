import face.config as config
import face.data as data
def main():
      # Load data
      data.DatasetBuilder(config.dataset_path).build_dataset()

if __name__ == "__main__":
      main()
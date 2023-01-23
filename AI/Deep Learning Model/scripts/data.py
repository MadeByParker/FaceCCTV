import facecctv_ai.config
import facecctv_ai.data

def main():
      # Load data

      facecctv_ai.data.DatasetBuilder(facecctv_ai.config.dataset_path).build_dataset()

if __name__ == "__main__":
      main()
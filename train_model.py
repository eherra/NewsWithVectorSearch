# train_model.py

# Import the main function from your script
from pipeline.model.train import main as train_main

def main():
    print("Starting the training process...")
    train_main()  # This calls your main training function
    print("Training has been completed.")

# This means that the script is being run directly (not being imported)
if __name__ == "__main__":
    main()

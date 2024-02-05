from datasets import load_sample_data
from n_gram import Tri_gram

def main():
    sample_data = load_sample_data()
    print(sample_data)
    my_model = Tri_gram()
    my_model.fit(sample_data)

if __name__ == "__main__":
    main()
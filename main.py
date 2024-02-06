from datasets import load_dataset

from n_gram import Tri_gram

def main():

    train_data = load_dataset('train2.csv')

    my_model = Tri_gram(use_smoothing=True)

    my_model.fit(train_data[:10])

    x = None    
    try:
        print(my_model.get_ppl("soft music played in the cozy cafe."))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
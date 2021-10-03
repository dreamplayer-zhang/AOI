import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
import random
col = 5


class QCSampling():

    def __init__(self) -> None:
        pass

    def Show(img):
        row = len(img) // col + 1
        plt.figure(figsize=(20, 3 * row))

        for i in range(len(img)):
            plt.subplot(row, col, i+1)
            plt.imshow(mpimg.imread('./test_images/test_images/' + img[i]))
            plt.xticks([])
            plt.yticks([])
            plt.title(img[i][5:-4])
        plt.show()

    # random choose {sample_num}, show the images and its probs. plot
    def RandomSample(sample_num, total_num, filepath, classes_indices):

        random_mother = [i for i in range(1, total_num+1)]
        random_list = random.sample(random_mother, sample_num)

        df = pd.read_csv(filepath)

        classes = [[] for _ in range(classes_indices)]
        for i in random_list:
            index = str(i)
            index = '0' * (5 - len(index)) + index

            # image's format : test_0000.jpg, for example
            target = f'test_{index}.jpg'
            label = df[df['ID'] == target]['Labels'].tolist()[0]
            classes[label].append(target)

        return classes

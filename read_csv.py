import pandas as pd
import numpy as np
import os.path as osp
import traceback

def get_std(array, ind, num_rounds):
    return np.std(array[ind: ind + num_rounds])

while True:
    try:
        threses = [0.5, 0.55]

        csv_path = input("run name: ")
        csv_path = osp.join('data', csv_path + '.csv')
        # csv_path = osp.join('fed-base', 'fed-base.csv')

        df = pd.read_csv(csv_path)
        values = np.array(df['Value'])
        steps = np.array(df['Step'])

        first_ind = -1
        for thres in threses:
            for ind, value in enumerate(values):
                if value >= thres:
                    first_ind = ind
                    break

            if first_ind != -1:
                first_step = steps[first_ind]
            else:
                first_step = 'NaN'
            print(f"Minimum step to reach accuracy={thres}: {first_step}")
            
        max_acc = values.max()
        print(f"Maximum accuracy: {max_acc}")

        std_thres = 0.01
        for ind, _ in enumerate(values):
            std = get_std(values, ind, 20)
            if std < std_thres:
                print(f"convergence round: {steps[ind]}")
                break
    except Exception as e:
        traceback.print_exc()
    finally:
        signal = input('Enter anything to continue, or q to exit')
        if signal == 'q':
            break

import numpy as np

from solver import captcha_setting, one_hot_encoding, my_dataset


# Batch decode
from solver.my_dataset import get_test_data_loader


def decode_captcha_batch(batch):
    out = []
    for j, _ in enumerate(batch):
        out.append(decode_captcha_single(batch[j]))
    return out

# Non-batch decode
def decode_captcha_single(prediction):
    c0 = captcha_setting.ALL_CHAR_SET[
        np.argmax(prediction[0:captcha_setting.ALL_CHAR_SET_LEN].data.numpy())]
    c1 = captcha_setting.ALL_CHAR_SET[np.argmax(
        prediction[captcha_setting.ALL_CHAR_SET_LEN:2 * captcha_setting.ALL_CHAR_SET_LEN].data.numpy())]
    c2 = captcha_setting.ALL_CHAR_SET[np.argmax(
        prediction[
        2 * captcha_setting.ALL_CHAR_SET_LEN:3 * captcha_setting.ALL_CHAR_SET_LEN].data.numpy())]
    c3 = captcha_setting.ALL_CHAR_SET[np.argmax(
        prediction[
        3 * captcha_setting.ALL_CHAR_SET_LEN:4 * captcha_setting.ALL_CHAR_SET_LEN].data.numpy())]
    return '%s%s%s%s' % (c0, c1, c2, c3)


def predict_n_batches(model, n=1, data_loader=get_test_data_loader(batch_size=64)):
    model.eval()
    test_dataloader = data_loader
    correct = 0
    total = 0
    batches_predicted = 0
    for i, (images, labels) in enumerate(test_dataloader):
        batches_predicted += 1
        predictions = model(images)
        predict_labels = decode_captcha_batch(predictions)
        for j, _ in enumerate(images):
            total += 1
            predict_label = predict_labels[j]
            true_label = one_hot_encoding.decode(labels[j].numpy())
            if predict_label == true_label:
                correct += 1
        print('Batch %d, %d test images, test Accuracy: %f %%' % (batches_predicted, total, 100 * correct / total))
        if batches_predicted >= n:
            break



import random


def random_points():
    count = 0
    x, y = [], []
    while count < 100:
        count += 1
        x.append(random.randint(-50, 50))
        y.append(random.randint(-50, 50))
    return tuple(zip(x, y))


def judge_quandrant(points):
    quandrant_1_cnt, quandrant_2_cnt, quandrant_3_cnt, quandrant_4_cnt, = 0, 0, 0, 0
    quandrant_1_tmp,quandrant_2_tmp,quandrant_3_tmp,quandrant_4_tmp = [],[],[],[]
    for i in range(len(points)):
        if points[i][0] > 0 and points[i][1] > 0:
            quandrant_1_cnt += 1
            quandrant_1_tmp.append(points[i])
        elif points[i][0] < 0 and points[i][1] > 0:
            quandrant_2_cnt += 1
            quandrant_2_tmp.append(points[i])
        elif points[i][0] < 0 and points[i][1] < 0:
            quandrant_3_cnt += 1
            quandrant_3_tmp.append(points[i])
        elif points[i][0] > 0 and points[i][1] < 0:
            quandrant_4_cnt += 1
            quandrant_4_tmp.append(points[i])
    print("第一象限点的数量为{0}，它们分别是{1}".format(quandrant_1_cnt, quandrant_1_tmp))
    print("第二象限点的数量为{0}，它们分别是{1}".format(quandrant_2_cnt, quandrant_2_tmp))
    print("第三象限点的数量为{0}，它们分别是{1}".format(quandrant_3_cnt, quandrant_3_tmp))
    print("第四象限点的数量为{0}，它们分别是{1}".format(quandrant_4_cnt, quandrant_4_tmp))


if __name__ == "__main__":
    points = random_points()
    judge_quandrant(points)

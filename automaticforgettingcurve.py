import matplotlib.pyplot as plt

def get_chapter_data():
    title = 'Why People Forget'
    content = 'Memory weakens over time without structured retrieval and regular review.'
    image_path = None
    return title, content, image_path

def create_forgetting_curve():
    d = [0, 1, 7, 30, 90]
    a = [100, 60, 40, 20, 10]
    b = [100, 90, 85, 80, 70]
    plt.figure(figsize=(6, 3))
    plt.plot(d, a, 'r-o', label="Without Review")
    plt.plot(d, b, 'g-o', label="With Review")
    plt.title('Forgetting Curve')
    plt.xlabel('Days')
    plt.ylabel('Retention %')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("forgetting_curve.png", dpi=300)
    plt.close()





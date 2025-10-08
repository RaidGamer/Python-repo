from matplotlib import pyplot as plt

def main():
    x = [3, 5, 7, 9]
    y = [5, 8, 11, 14]
    plt.plot(x, y, c="red", linewidth=2, label="Linje 1")

    x2 = [1, 3, 5, 7]
    y2 = [3, 6, 7, 9]
    plt.plot(x2, y2, c="green", linewidth=2, label="Linje 2", linestyle="dashed", marker="o", markerfacecolor="navy", markersize=10) #marker kan också vara lika med "s" för fyrkantiga makrörer

    plt.xlabel("X-Axel")
    plt.ylabel("Y-Axeln")
    plt.title("Två Linjer...")

    plt.ylim(0, 10) #sätter begränsningar för axlarna för hur de ska visas
    plt.xlim(0,30)

    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
from bs4 import BeautifulSoup

def get_text(filename: str) -> str:
    with open(filename, encoding="utf-8") as file:
        soup = BeautifulSoup(file.read(), "html.parser")
        return soup.get_text()
    
def count_nines(text: str) -> int:
    return text.count("9")

if __name__ == "__main__":
    # räkna i den lilla filen
    # small_text = get_text("SmallNines.csv")
    # print("Amount of nines in small > " ,count_nines(small_text))

    # räkna i den stora filen
     large_text = get_text("LargeNines.csv")
     print("Amount of nines in large > " ,count_nines(large_text))



import json

def load_json_data():
    home_dict_data = list()
    with open ("data.json","r") as json_in:
        json_data = json.load(json_in)
    home_dict_data.extend(json_data)
    return home_dict_data

def write_json_data(json):
    with open("data.json",w) as json_out:
        json.dump(json_data,json_out)

class Homework:
    def __init__(self, name, priority, completed=False):
        self.name = name
        self.priority = priority
        self.completed = completed

class HomeworkList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def all_completed(self):
        completed = True
        for item in self.items:
            if item.completed == False:
                completed = False
                print(item.name)
        if completed:
            print("All finished!")

    def show_items(self):
        if not self.items:
            print("Danh sách bài tập trống.")
        else:
            for i, item in enumerate(self.items, 1):
                status = "Hoàn thành" if item.completed else "Chưa hoàn thành"
                print(f"{i}. {item.name} (Ưu tiên: {item.priority}) - {status}")

    def remove_item(self, name):
        found = False
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                found = True
                print(f"Đã xoá bài tập: {name}")
                break
        if not found:
            print(f"Không tìm thấy bài tập: {name}")

    def mark_completed(self, name):
        found = False
        for item in self.items:
            if item.name == name:
                item.completed = True
                found = True
                print(f"Đã đánh dấu hoàn thành: {name}")
                break
        if not found:
            print(f"Không tìm thấy bài tập: {name}")
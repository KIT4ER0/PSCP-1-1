"""iPhone 13 Again"""
def mini(storage):
    """13"""
    if storage == "128 GB":
        return 25900
    elif storage == "256 GB":
        return 29900
    elif storage == "512 GB":
        return 37900
    else:
        return "Not Available"
def normal(storage):
    """13"""
    if storage == "128 GB":
        return 29900
    elif storage == "256 GB":
        return 33900
    elif storage == "512 GB":
        return 41900
    else:
        return "Not Available"
def pro(storage):
    """pro"""
    if storage == "128 GB":
        return 38900
    elif storage == "256 GB":
        return 42900
    elif storage == "512 GB":
        return 50900
    elif storage == "1 TB":
        return 58900
    else:
        return "Not Available"
def pro_max(storage):
    """pro max"""
    if storage == "128 GB":
        return 42900
    elif storage == "256 GB":
        return 46900
    elif storage == "512 GB":
        return 54900
    elif storage == "1 TB":
        return 62900
    else:
        return "Not Available"
def main():
    """iPhone 13 Again"""
    model_name = input()
    in_storage = input()
    if model_name == "iPhone 13 mini":
        print(mini(in_storage))
    elif model_name == "iPhone 13":
        print(normal(in_storage))
    elif model_name == "iPhone 13 Pro":
        print(pro(in_storage))
    elif model_name == "iPhone 13 Pro Max":
        print(pro_max(in_storage))
    else:
        print("Not Available")
main()

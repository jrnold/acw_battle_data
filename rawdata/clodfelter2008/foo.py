import yaml
from os import path

with open(path.expanduser("~/Downloads/clodfelter.yaml"), "r") as f:
    data = yaml.load(f)

theaters = ("Eastern Theater: 1861", "Western Theater: 1861",
            "Blockade War: 1861-1862", "East: 1862", "West: 1862",
            "East: 1863", "West: 1863", "Blockade War: 1863",
            "East: 1864", "West: 1864", "Blockade War: 1864-65",
            "East: 1865", "West: 1865")
newdata = []
for k in theaters:
    for btl in data[k]:
        btl['theater'] = k
        newdata.append(btl)

with open("clodfelter.yaml", "w") as f:
    yaml.dump(newdata, f, default_flow_style = False)

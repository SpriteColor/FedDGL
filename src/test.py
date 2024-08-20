import pickle

data = {"label" : {"DBLP5" : {"w_local" : { "fedavg":[1.08, 1.09], "fedavgdyn":[1.01, 1.02], 
                        "fedsage":[1.10, 1.11], "fedsagedyn":[1.034, 1.044], 
                        "fedproto":[1.11, 1.12], "fedprotodyn":[1.055, 1.065],
                        "fedego":[1.10, 1.11], "fedgcn":[1.06, 1.07], 
                        "dfedgnn":[1.11, 1.12], "mine":[1.07, 1.08],
                        "mine_kd":[1.02, 1.03], "mine_gp":[1.03, 1.04],
                        "mine_pa":[1.05, 1.06]
                        },
                    "w_global" : { "fedavg":[0.89, 0.90], "fedavgdyn":[0.86, 0.87], 
                        "fedsage":[0.93, 0.94], "fedsagedyn":[0.87, 0.88], 
                        "fedproto":[0.95, 0.96], "fedprotodyn":[0.89, 0.90],
                        "fedego":[0.94, 0.95], "fedgcn":[0.88, 0.89], 
                        "dfedgnn":[0.94, 0.95], "mine":[0.92, 0.93],
                        "mine_kd":[0.855, 0.865], "mine_gp":[0.86, 0.87],
                        "mine_pa":[0.89, 0.90]} },


        "DBLP3" : {"w_local" : { "fedavg":[1.06, 1.07], "fedavgdyn":[0.69, 0.70], 
                        "fedsage":[1.10, 1.11], "fedsagedyn":[0.72, 0.73], 
                        "fedproto":[1.14, 1.15], "fedprotodyn":[0.74, 0.75],
                        "fedego":[1.12, 1.13], "fedgcn":[1.05, 1.06], 
                        "dfedgnn":[1.10, 1.11], "mine":[0.75, 0.76],
                        "mine_kd":[0.68, 0.69], "mine_gp":[0.69, 0.70],
                        "mine_pa":[0.73, 0.74]},
                    "w_global" : {"fedavg":[0.90, 0.91], "fedavgdyn":[0.62, 0.63], 
                                "fedsage":[0.95, 0.96], "fedsagedyn":[0.64, 0.65], 
                                "fedproto":[1.00, 1.01], "fedprotodyn":[0.66, 0.67],
                                "fedego":[1.01, 1.02], "fedgcn":[0.90, 0.91],
                                "dfedgnn":[0.95, 0.96], "mine":[0.68, 0.69],
                                "mine_kd":[0.61, 0.62], "mine_gp":[0.615, 0.625],
                                "mine_pa":[0.65, 0.66]} },
        
        "Brain" : {"w_local" : { "fedavg":[1.16, 1.17], "fedavgdyn":[0.80, 0.81], 
                        "fedsage":[1.20, 1.21], "fedsagedyn":[0.82, 0.83], 
                        "fedproto":[1.24, 1.25], "fedprotodyn":[0.84, 0.85],
                        "fedego":[1.32, 1.33], "fedgcn":[1.07, 1.08], 
                        "dfedgnn":[1.38, 1.39], "mine":[0.86, 0.87],
                        "mine_kd":[0.80, 0.81], "mine_gp":[0.81, 0.82],
                        "mine_pa":[0.84, 0.85]},
                    "w_global" : {"fedavg":[0.90, 0.91], "fedavgdyn":[0.62, 0.63], 
                                "fedsage":[0.95, 0.96], "fedsagedyn":[0.64, 0.65], 
                                "fedproto":[1.00, 1.01], "fedprotodyn":[0.66, 0.67],
                                "fedego":[1.11, 1.12], "fedgcn":[0.80, 0.81], 
                                "dfedgnn":[1.10, 1.11], "mine":[0.71, 0.72],
                                "mine_kd":[0.655, 0.665], "mine_gp":[0.66, 0.67],
                                "mine_pa":[0.68, 0.69]} },

        "Reddit" : {"w_local" : { "fedavg":[1.20, 1.21], "fedavgdyn":[0.65, 0.66], 
                        "fedsage":[1.24, 1.25], "fedsagedyn":[0.69, 0.70], 
                        "fedproto":[1.28, 1.29], "fedprotodyn":[0.71, 0.72],
                        "fedego":[1.34, 1.35], "fedgcn":[1.18, 1.19], 
                        "dfedgnn":[1.24, 1.25], "mine":[0.73, 0.74],
                        "mine_kd":[0.65, 0.66], "mine_gp":[0.66, 0.67],
                        "mine_pa":[0.70, 0.71]},
                    "w_global" : {"fedavg":[0.94, 0.95], "fedavgdyn":[0.55, 0.56], 
                                "fedsage":[0.99, 1.00], "fedsagedyn":[0.57, 0.58], 
                                "fedproto":[1.04, 1.05], "fedprotodyn":[0.59, 0.60],
                                "fedego":[1.10, 1.11], "fedgcn":[0.90, 0.91], 
                                "dfedgnn":[0.97, 0.98], "mine":[0.62, 0.63],
                                "mine_kd":[0.54, 0.55], "mine_gp":[0.55, 0.56],
                                "mine_pa":[0.59, 0.60]}}},

    "louvain" : {"DBLP5" : {"w_local" : {'fedavg': [0.8250000000000001, 0.8350000000000001], 'fedavgdyn': [0.79, 0.8], 'fedsage': [0.8300000000000001, 0.8400000000000001], 'fedsagedyn': [0.8, 0.81], 'fedproto': [0.8350000000000001, 0.8450000000000001], 'fedprotodyn': [0.81, 0.8200000000000001], 'fedego': [0.86, 0.87], 'mine': [0.8200000000000001, 0.8300000000000001], 'fedgcn': [0.8400000000000001, 0.8500000000000001], 'dfedgnn': [0.86, 0.87]},
    "w_global" : {'fedavg': [0.86, 0.87], 'fedavgdyn': [0.82, 0.83], 'fedsage': [0.87, 0.88], 'fedsagedyn': [0.83, 0.84], 'fedproto': [0.89, 0.8999999999999999], 'fedprotodyn': [0.83, 0.84], 'fedego': [0.8999999999999999, 0.9099999999999999], 'mine': [0.86, 0.87], 'fedgcn': [0.83, 0.84], 
    'dfedgnn': [0.88, 0.89]}},

    "DBLP3" : {"w_local" : {'fedavg': [0.895, 0.905], 'fedavgdyn': [0.62, 0.63], 'fedsage': [0.9, 0.91], 'fedsagedyn': [0.63, 0.64], 'fedproto': [0.91, 0.9199999999999999], 'fedprotodyn': [0.64, 0.65], 'fedego': [0.9299999999999999, 0.94], 'mine': [0.64, 0.65], 'fedgcn': [0.9299999999999999, 0.94], 'dfedgnn': [0.9299999999999999, 0.94]},
    "w_global" : {'fedavg': [0.87, 0.88], 'fedavgdyn': [0.59, 0.6], 'fedsage': [0.88, 0.89], 'fedsagedyn': [0.61, 0.62], 'fedproto': [0.89, 0.8999999999999999], 'fedprotodyn': [0.61, 0.62], 'fedego': [0.9199999999999999, 0.9299999999999999], 'mine': [0.63, 0.64], 'fedgcn': [0.86, 0.87], 'dfedgnn': [0.9099999999999999, 0.9199999999999999]}},

    "Brain" : {"w_local" : {'fedavg': [0.86, 0.87], 'fedavgdyn': [0.61, 0.62], 'fedsage': [0.88, 0.89], 'fedsagedyn': [0.615, 0.625], 'fedproto': [0.89, 0.8999999999999999], 'fedprotodyn': [0.63, 0.64], 'fedego': [1.07, 1.08], 'mine': [0.6499999999999999, 0.6599999999999999], 'fedgcn': [0.88, 0.89], 
    'dfedgnn': [1.04, 1.05]},
    "w_global" : {'fedavg': [0.86, 0.87], 'fedavgdyn': [0.62, 0.63], 'fedsage': [0.88, 0.89], 'fedsagedyn': [0.63, 0.64], 'fedproto': [0.9, 0.91], 'fedprotodyn': [0.64, 0.65], 'fedego': [1.09, 1.1], 'mine': [0.6699999999999999, 0.6799999999999999], 'fedgcn': [0.8099999999999999, 0.82], 'dfedgnn': [1.08, 1.09]}},

    "Reddit" : {"w_local" : {'fedavg': [1.05, 1.06], 'fedavgdyn': [0.6, 0.61], 'fedsage': [1.07, 1.08], 'fedsagedyn': [0.62, 0.63], 'fedproto': [1.11, 1.12], 'fedprotodyn': [0.64, 0.6499999999999999], 'fedego': [1.1500000000000001, 1.1600000000000001], 'mine': [0.6699999999999999, 0.6799999999999999], 'fedgcn': [1.1600000000000001, 1.1500000000000001], 'dfedgnn': [1.11, 1.12]},
    "w_global" : {'fedavg': [0.8999999999999999, 0.9099999999999999], 'fedavgdyn': [0.49000000000000005, 0.5], 'fedsage': [0.9299999999999999, 0.94], 'fedsagedyn': [0.51, 0.52], 'fedproto': [0.97, 0.98], 'fedprotodyn': [0.53, 0.54], 'fedego': [0.98, 0.99], 'mine': [0.56, 0.5700000000000001], 'fedgcn': [0.8600000000000001, 0.8700000000000001], 'dfedgnn': [0.96, 0.97]}}}}



# with open('test.cpython-39.pkl', 'wb') as f:
#     pickle.dump(data, f)

def getData():
    try:
        with open('test.cpython-39.pkl', 'rb') as f:
            data = pickle.load(f)
            return data
    except FileNotFoundError:
        try:
            with open('../test.cpython-39.pkl', 'rb') as f:
                data = pickle.load(f)
                return data
        except FileNotFoundError:
            try:
                with open('module/model/__pycache__/test.cpython-39.pkl', 'rb') as f:
                    data = pickle.load(f)
                    return data
            except FileNotFoundError:
                try:
                    with open('src/module/model/__pycache__/test.cpython-39.pkl', 'rb') as f:
                        data = pickle.load(f)
                        return data
                except FileNotFoundError:
                    data = {"label" : {"DBLP5" : {"w_local" : {}, "w_global" : {} }, "DBLP3" : {"w_local" : {}, "w_global" : {} },
                    "Brain" : {"w_local" : {}, "w_global" : {} }, "Reddit" : {"w_local" : {}, "w_global" : {}}},
                    "louvain" : {"DBLP5" : {"w_local" : {}, "w_global" : {}}, "DBLP3" : {"w_local" : {}, "w_global" : {}},
                    "Brain" : {"w_local" : {}, "w_global" : {}}, "Reddit" : {"w_local" : {}, "w_global" : {}}}}
                    return data


data = getData()
print(data)
print(data["label"]["DBLP5"]["w_local"], data["label"]["DBLP5"]["w_global"])

if "fedstar" not in data["label"]["DBLP5"]["w_local"]:
    print("no element")
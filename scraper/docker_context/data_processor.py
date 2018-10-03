class DataProcessor:

    def structured_data_point(self, ip, line, cutting_index):
        data_point = {"computer_ip": ip, "data_type": line[:cutting_index]}
        data_string = line[cutting_index:]
        index = data_string.find("}")
        data_arr = data_string[1:index].split(",")

        for d in data_arr:
            d_split = d.split("=")
            data_point[d_split[0]] = eval(d_split[1])
        value = eval(data_string[index + 1:].strip())
        data_point["value"] = value
        return data_point

    def single_value_data_point(self, ip, line):
        data_point = {"computer_ip": ip}
        data = line.split()
        data_point["data_type": data[0], "value": eval(data[1])]
        return data_point

    def process_line(self, ip, line):
        if line.find("{") == -1:
            return self.single_value_data_point(ip, line)
        else:
            data = line.split("{")
            return self.structured_data_point(ip, line, len(data[0]))

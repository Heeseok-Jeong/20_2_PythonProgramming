# 사람들의 체온 기록
# 1. dict로 체온 범위 테이블 생성,

age_group_list = ["0-2 Years", "3-10 Years", "11-65 Years", "> 65 Years"]
msmt_site_list = ["Ear", "Oral", "Rectal", "Acillary"]

def is_valid_input(input_list):
    


temperature_range_table = {}
temperature_range_table[age_group_list[0]] = {msmt_site_list[1] : [36.4, 38.0], msmt_site_list[2] : [36.6, 38.0], msmt_site_list[3] : [34.7, 37.3]}
temperature_range_table[age_group_list[1]] = {msmt_site_list[0] : [35.5, 37.5], msmt_site_list[1] : [36.1, 37.8], msmt_site_list[2] : [36.6, 38.0], msmt_site_list[3] : [35.9, 36.7]}
temperature_range_table[age_group_list[2]] = {msmt_site_list[0] : [36.4, 37.6], msmt_site_list[1] : [35.9, 37.6], msmt_site_list[2] : [37.0, 38.1], msmt_site_list[3] : [35.2, 36.9]}
temperature_range_table[age_group_list[3]] = {msmt_site_list[0] : [35.8, 36.9], msmt_site_list[1] : [35.8, 37.5], msmt_site_list[2] : [36.2, 37.3], msmt_site_list[3] : [35.6, 36.3]}

print("This is Body Temperature program. Welcome :)\n")
input_ment = "Enter three values <Age group, Measurement site, Body temperature>\n"
input_ment += "You should enter each value exactly matched below conditions.\n"
input_ment += "Age group : " + str(age_group_list) + ",\n"
input_ment += "Measurement site : " + str(msmt_site_list) + ",\n"
input_ment += "Body temperature : positive real number.\n"
input_ment += "Keep in mind there are comma between values (ex. 0-2 Years, Rectal, 36.5)\n"
input_ment += "Input : "
input_list = input(input_ment).split(', ')
print(input_list)

if is_valid_input(input_list):
    prit("valid")
# print(age_group, msmt_site, body_temp)

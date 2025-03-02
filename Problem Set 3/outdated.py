months  = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
ans = ""
while True:
    try:
        date = input("Date: ")
        print()
        if (date[0]).isdigit() and int(date.split("/")[0]) in months.values():
            month, day, year = date.split("/")
            month_int = int(month)
            day_int = int(day)
            
            if 0 < day_int < 32  and len(month) == 1:
                ans += year + "-" + "0" + month + "-" 
            elif 0 < day_int < 32 and len(month) == 2:
                ans += year + "-" + month + "-"
            
            if 0 < day_int < 32 and len(day) == 1:
                ans += "0" + day  
                break
            elif 0 < day_int < 32 and len(day) == 2:
                ans += day
                break
                    
                    
        elif date.split(" ")[0] in months:
            month, dayK, year = date.split(" ")
            day = dayK.split(",")[0]
            
            for key, value in months.items():
                if key == month:
                    monthprop = value

            mon_str = str(monthprop)
            day_int = int(day)
            
            if 0 < day_int < 32  and len(mon_str) == 1:
                ans += year + "-" + "0" + mon_str + "-"
            elif 0 < day_int < 32 and len(mon_str) == 2:
                ans += year + "-" + mon_str + "-" 
                  
            if 0 < day_int < 32 and len(day) == 1:
                ans += "0" + day
                break
            elif 0 < day_int < 32 and len(day) == 2:
                ans += day
                break
    except EOFError:
        print()
        break
    
print(ans)
                
                
                
                
                
                
                
            
        
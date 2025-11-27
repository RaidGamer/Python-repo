import requests
import json


def interpol():
    headers = {
        "User-agent":"Mozilla/5.0",
        "Accept":"application/json"
    }

    url = "https://ws-public.interpol.int/notices/v1/red"

    pageStr = input("page: ")
    maxPageStr = input("maxPage: ")
    all_text = ""
    if not {pageStr.isdigit() and maxPageStr.isdigit() and int(pageStr) < int(maxPageStr)}:
        page = 1
        maxPage = 3
    else:
        page = int(pageStr)
        maxPage = int(maxPageStr)

    while page <= maxPage:
        params = {
        "page":page,
        "resultPerPage":1,
        }
        notice = requests.get(url, headers=headers, params=params).json()
        url2 = notice["_embedded"]["notices"][0]["_links"]["self"]["href"]
        noticeDetailed = requests.get(url2, headers=headers).json()

        def safe_get(d, key, default="N/A"):
            return d.get(key, default)
        #ren info
        
        forename = safe_get(noticeDetailed, "forename")
        lastname = safe_get(noticeDetailed, "name")
        gender = safe_get(noticeDetailed, "sex_id")
        id = safe_get(noticeDetailed, "entity_id")
        weight = safe_get(noticeDetailed, "weight")
        height = safe_get(noticeDetailed, "height")
        dob = safe_get(noticeDetailed, "date_of_birth")

        nationalitiesList = noticeDetailed.get("nationalities") or []
        nationalities = ", ".join(nationalitiesList) if isinstance(nationalitiesList, list) else str(nationalitiesList)
        
        arrest_warrants = noticeDetailed.get("arrest_warrants") or [{}]
        charge = safe_get(arrest_warrants[0], "charge")
        issuedCountry = safe_get(arrest_warrants[0], "issuing_country_id")

        #info printas us
        info = f"""
        NOTICE {page}:
            ID: {id}
            Fullname: {f"{forename} {lastname}"}
            Gender: {gender}
            Physical: 
                weight: {weight}
                height: {height}
            Date of birth: {dob}
            Nationalities: {nationalitiesList}
            Charge details:
                charge: {charge}
                charge issued by: {issuedCountry}
    """
        print("="*50)
        print(info)
        
        all_text += "="*50 + "\n" + info + "\n"


        page += 1
    return all_text

def main():
    text = interpol()
    print("output från interpol() nedanför")
    print(text)
    toFile = input("Save to text to desktop? y/n: ").lower()
    if toFile == "y":
        fileName = input("Name to save file to: ")
        import os
        file_path = os.path.expanduser(f"~/Desktop/{fileName}")
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            file.write(text)
    else:
        print("Demon - Im not in the mirror im inside you, let me guide you.\nEminem - No die you stupid son of a bitch.\nDemon - Put the gun down.\nEminem - bye bye!!\n*Shoots\nEminem - Huh?! Im still alive!\nDemon - So am I too..")
        


main()



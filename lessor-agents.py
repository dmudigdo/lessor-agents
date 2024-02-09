import requests, bs4

# Web:
cookies = {
    'reauid': '8d9654b8e05a01004e8d8f65ba0100001ef11b00',
    'utag_main': 'v_id:018cb8c010210010106e1a52a2670504600350090086e$_sn:3$_se:1$_ss:1$_st:1707391968640$vapi_domain:realestate.com.au$dc_visit:3$ses_id:1707390168640%3Bexp-session$_pn:1%3Bexp-session$_prevpage:rea%3Arent%3Asearch%20result%20-%20list%3Bexp-1707393769755$dc_event:1%3Bexp-session$dc_region:ap-southeast-2%3Bexp-session',
    'split_audience': 'b',
    'AMCV_341225BE55BBF7E17F000101%40AdobeOrg': '-330454231%7CMCIDTS%7C19762%7CMCMID%7C47234961578617247253515664118391607453%7CMCAID%7CNONE%7CMCOPTOUT-1707397370s%7CNONE%7CMCAAMLH-1707994970%7C8%7CMCAAMB-1707994970%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19769%7CvVersion%7C3.1.2',
    '_sp_id.2fe7': 'fa9799ca-3e69-4a1f-9dcb-8147467939fd.1703906648.3.1707390170.1707379785.fb20f89b-6b6b-4e7d-81c1-6ff5f66311ab',
    'VT_LANG': 'language%3Den-US',
    'mid': '15933649636612828640',
    '_gcl_au': '1.1.1235941294.1703906653',
    '_ga_F962Q8PWJ0': 'GS1.1.1707390172.3.0.1707390172.0.0.0',
    '_ga': 'GA1.3.753389878.1703906653',
    '_ga_3J0XCBB972': 'GS1.1.1707390172.3.0.1707390172.0.0.0',
    's_ecid': 'MCMID%7C47234961578617247253515664118391607453',
    '_fbp': 'fb.2.1703906657177.1959988297',
    'nol_fpid': '40agazoxd8fc98bzorshldugtgpvx1703906662|1703906662102|1707390175725|1707390175980',
    'KP_UIDz-ssn': '08e2ISP8FwCD11miAOeSzQdEeSVDXGW6i3VHa7AjvPan3nBBj5epILVDH3FbZCM58ENDdEcm69gaiBX61i0EHjKWPufrYAcsq82gDjPV3o1eYAH4F0vedN9OptGhVbCe7NssW81AQjyRQAlbUZrgF1vy8ulYdTy',
    'KP_UIDz': '08e2ISP8FwCD11miAOeSzQdEeSVDXGW6i3VHa7AjvPan3nBBj5epILVDH3FbZCM58ENDdEcm69gaiBX61i0EHjKWPufrYAcsq82gDjPV3o1eYAH4F0vedN9OptGhVbCe7NssW81AQjyRQAlbUZrgF1vy8ulYdTy',
    's_nr30': '1707390169761-Repeat',
    'topid': 'REAUID:8D9654B8E05A01004E8D8F65BA0100001EF11B00',
    '_lr_geo_location_state': 'WA',
    '_lr_geo_location': 'AU',
    '_gid': 'GA1.3.1621759769.1707378096',
    'Country': 'AU',
    'fullstory_audience_split': 'B',
    'pageview_counter.srs': '1',
    '_sp_ses.2fe7': '*',
    'AMCVS_341225BE55BBF7E17F000101%40AdobeOrg': '1',
    's_cc': 'true',
    'myid5_id': 'ID5*y_oy-BAeB10ADPxpiHhpDdsiIgrEFgZXmdOMODDOpfWCxDp9sWbfdEaEjzc8JZE6gsX6bly-Xs4rjOVYWLyTuA',
    'DM_SitId1464': '1',
    'DM_SitId1464SecId12708': '1',
    'QSI_HistorySession': 'https%3A%2F%2Fwww.realestate.com.au%2Frent%2Fin-carlisle%2C%2Bwa%2B6101%2Flist-1~1707390173172',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'reauid=8d9654b8e05a01004e8d8f65ba0100001ef11b00; utag_main=v_id:018cb8c010210010106e1a52a2670504600350090086e$_sn:3$_se:1$_ss:1$_st:1707391968640$vapi_domain:realestate.com.au$dc_visit:3$ses_id:1707390168640%3Bexp-session$_pn:1%3Bexp-session$_prevpage:rea%3Arent%3Asearch%20result%20-%20list%3Bexp-1707393769755$dc_event:1%3Bexp-session$dc_region:ap-southeast-2%3Bexp-session; split_audience=b; AMCV_341225BE55BBF7E17F000101%40AdobeOrg=-330454231%7CMCIDTS%7C19762%7CMCMID%7C47234961578617247253515664118391607453%7CMCAID%7CNONE%7CMCOPTOUT-1707397370s%7CNONE%7CMCAAMLH-1707994970%7C8%7CMCAAMB-1707994970%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19769%7CvVersion%7C3.1.2; _sp_id.2fe7=fa9799ca-3e69-4a1f-9dcb-8147467939fd.1703906648.3.1707390170.1707379785.fb20f89b-6b6b-4e7d-81c1-6ff5f66311ab; VT_LANG=language%3Den-US; mid=15933649636612828640; _gcl_au=1.1.1235941294.1703906653; _ga_F962Q8PWJ0=GS1.1.1707390172.3.0.1707390172.0.0.0; _ga=GA1.3.753389878.1703906653; _ga_3J0XCBB972=GS1.1.1707390172.3.0.1707390172.0.0.0; s_ecid=MCMID%7C47234961578617247253515664118391607453; _fbp=fb.2.1703906657177.1959988297; nol_fpid=40agazoxd8fc98bzorshldugtgpvx1703906662|1703906662102|1707390175725|1707390175980; KP_UIDz-ssn=08e2ISP8FwCD11miAOeSzQdEeSVDXGW6i3VHa7AjvPan3nBBj5epILVDH3FbZCM58ENDdEcm69gaiBX61i0EHjKWPufrYAcsq82gDjPV3o1eYAH4F0vedN9OptGhVbCe7NssW81AQjyRQAlbUZrgF1vy8ulYdTy; KP_UIDz=08e2ISP8FwCD11miAOeSzQdEeSVDXGW6i3VHa7AjvPan3nBBj5epILVDH3FbZCM58ENDdEcm69gaiBX61i0EHjKWPufrYAcsq82gDjPV3o1eYAH4F0vedN9OptGhVbCe7NssW81AQjyRQAlbUZrgF1vy8ulYdTy; s_nr30=1707390169761-Repeat; topid=REAUID:8D9654B8E05A01004E8D8F65BA0100001EF11B00; _lr_geo_location_state=WA; _lr_geo_location=AU; _gid=GA1.3.1621759769.1707378096; Country=AU; fullstory_audience_split=B; pageview_counter.srs=1; _sp_ses.2fe7=*; AMCVS_341225BE55BBF7E17F000101%40AdobeOrg=1; s_cc=true; myid5_id=ID5*y_oy-BAeB10ADPxpiHhpDdsiIgrEFgZXmdOMODDOpfWCxDp9sWbfdEaEjzc8JZE6gsX6bly-Xs4rjOVYWLyTuA; DM_SitId1464=1; DM_SitId1464SecId12708=1; QSI_HistorySession=https%3A%2F%2Fwww.realestate.com.au%2Frent%2Fin-carlisle%2C%2Bwa%2B6101%2Flist-1~1707390173172',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}
exfile = requests.get("https://www.realestate.com.au/rent/in-carlisle,+wa+6101/list-2",headers=headers,cookies=cookies)
print(exfile.status_code)
# exfile.raise_for_status()
exsoup = bs4.BeautifulSoup(exfile.text,'html.parser')

# Local:
# exfile = open('agents.html')
# exsoup = bs4.BeautifulSoup(exfile,'html.parser')


agents = exsoup.find_all("img", {"class": "branding__image"})

ag_freq = dict()

for tag in agents:
    agent = tag['alt']
    if agent in ag_freq:
        ag_freq[agent]+=1   
    else:
        ag_freq[agent]=1

for brand in ag_freq:
    print(brand,",", ag_freq[brand])

import json
from django.http import JsonResponse
from django.shortcuts import render

from AnonymousIsland.models import USER
from AnonymousIsland.models import NOTE

###### GLOBAL_VARIABLE

map_info = {
    "lng": {"min": 116.2, "max": 116.5},
    "lat": {"min": 39.8, "max": 40},
    "step": 0.02,
    "zoom": 18
}

###### PRODUCTION_UNITED_SELECT

def get_data(request):
    global map_info
    raw_data = USER.objects.all()
    map_info['blocks'] = []
    for i in raw_data:
        temp_blocks = {
            "id": i.id,
            "rect":
                {
                    "left-up": {"lng": i.LEFT_UP_LNG, "lat": i.LEFT_UP_LAT},
                    "right-up": {"lng": i.RIGHT_UP_LNG, "lat": i.RIGHT_UP_LAT},
                    "right-down": {"lng": i.RIGHT_DOWN_LNG, "lat": i.RIGHT_DOWN_LAT},
                    "left-down": {"lng": i.LEFT_DOWN_LNG, "lat": i.LEFT_DOWN_LAT},
                    "center": {"lng": i.CENTER_LNG, "lat": i.CENTER_LAT},
                }
        }
        map_info['blocks'].append(temp_blocks)
    row_data = USER.objects.raw(
        "select observationpivot_block.id,count(observationpivot_note.BLOCKID) as len from observationpivot_block left join observationpivot_note on observationpivot_block.id = observationpivot_note.BLOCKID GROUP BY observationpivot_block.id order by id;")
    map_info['block_list']=[{"id":int(n.id),"len":int(n.len)} for n in row_data]
    map_info['timestamp']=[]
    map_info['timestamp'].append({"localtime": get_local_time()})
    return JsonResponse(map_info)


###### PRODUCTION_SINGLE_SELECT

def index(request):
    controller_to_view=[]
    return render(request, "index.html", {"metadata": controller_to_view})

def get_note(request):
    ## INIT
    request.encoding = 'utf-8'
    blockid_content = ""
    if 'blockid' in request.GET:
        blockid_content = int(request.GET['blockid'])

    ## GET DATA
    note_select = NOTE.objects.filter(BLOCKID=blockid_content)
    count_note_item = 0
    current_note_item = 0
    for note_item in note_select:
        count_note_item += 1
    Json_text = "{\"note\":["
    for note_item in note_select:
        Json_text += '\"'
        strtemp=""
        Json_text += strtemp.join(note_item.NOTEDATA) ########有和谐
        Json_text += '\"'
        current_note_item += 1
        if current_note_item != count_note_item:
            Json_text += ","
    Json_text += "]}"
    Json_Json = json.loads(Json_text)
    return JsonResponse(Json_Json)


def put_note(request):
    ## INIT
    request.encoding = 'utf-8'
    blockid_content = ""
    userdata_content = ""

    ## GET BODY
    if 'blockid' in request.GET:
        blockid_content = request.GET['blockid']
    if 'userdata' in request.GET:
        userdata_content = request.GET['userdata']
    controller_to_view = [blockid_content, userdata_content]

    if request.GET['blockid'] == "" or request.GET['userdata'] == "":
        return JsonResponse(
            {
                "status": "failed",
                "code": "401",
                "content": {
                    "blockid": controller_to_view[0],
                    "userdata": controller_to_view[1]
                }
            }
        )
    else:
        if len(request.GET['userdata']) > 301:
            return JsonResponse(
                {
                    "status": "failed",
                    "code": "500",
                    "content": {
                        "blockid": controller_to_view[0],
                        "userdata": "too long"
                    }
                }
            )
        elif Is_Int(request.GET['blockid']) != True:
            return JsonResponse(
                {
                    "status": "failed",
                    "code": "500",
                    "content": {
                        "blockid": controller_to_view[0],
                        "userdata": "blockid not integer"
                    }
                }
            )
        else:
            note_insert = NOTE(BLOCKID=int(blockid_content), NOTEDATA=userdata_content)
            note_insert.save()
            return JsonResponse(
                {
                    "status": "success",
                    "code": "200",
                    "content": {
                        "blockid": controller_to_view[0],
                        "userdata": controller_to_view[1]
                    }
                }
            )


def get_build_data(request):
    return JsonResponse(
        {
            "lng": {"min": 116.2, "max": 116.5},
            "lat": {"min": 39.8, "max": 40},
            "step": 0.02,
            "zoom": 18
        }
    )

###### GENERATE_DATA

# def fun(n):
#     if type(n) is int:
#         return n
#     k = 10000
#     n *= k
#     n = int(n)
#     return n / k
#
#
# def export(data):
#     header = [n for n in data[0]]
#     header_str = ",".join([f"\"{n}\"" for n in header])
#     with open('observationpivot_block.csv', 'w', encoding='utf-8')as f:
#         f.write(header_str + '\n')
#         for item in data:
#             mid = [f"\"{fun(item[n])}\"" for n in item]
#             f.write(",".join(mid) + "\n")
#
#
# # 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     export(build_data())
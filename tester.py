import json
with open("/Users/teresabehr/Downloads/92dc32e5-72dd-444c-a671-391ef5f7429f.json", "r") as f:
    ch = json.load(f)
# ch = json.loads("/Users/teresabehr/Downloads/d8533d0c-234a-41a4-8515-c5f9425b3cc8.json")

callIds = []

for item in ch["conversationFlow"]:
    # print(item["request"]["callMeta"]["callId"])


    if item["request"]["callMeta"]["callId"] not in callIds:
        # print("appended!")
        callIds.append(item["request"]["callMeta"]["callId"])

# print(callIds)

calls = {item:{} for item in callIds}

# print(calls)

for item in ch["conversationFlow"]:

    calls[item["request"]["callMeta"]["callId"]][item["timestamp"]] = {
        "human": item["human"]["message"],
        "bot": item["bot"]["message"]
    }

    print("")

for call in calls.values():
    call = dict(sorted(call.items()))

# print(calls)

for call in calls.values():
    for turn in call.values():
        print(turn)
    print("")



# for turn in sorted_conv.values():
#     print(turn)

# timestamped = {}

# for item in ch["conversationFlow"]:

#     timestamped[item["timestamp"]] = {
#         "human": item["human"]["message"],
#         "bot": item["bot"]["message"]
#     }

#     print("")

# sorted_conv = dict(sorted(timestamped.items()))

# for turn in sorted_conv.values():
#     print(turn)


# # print(ch)


from datetime import datetime

reply1 = {
    "Text": "Was there earlier, the staff is very friendly too!",
    "Name": "Elena Kurkova",
    "DateTime": datetime(2022, 3, 25),
    "Picture": "elena.png"
}

comment1 = {
    "CommentId": 1,
    "Text": "Clean place, has anticeptic",
    "Name": "Barbara Middleton",
    "Likes": ["Elena Kurkova"],
    "Comments": [reply1],
    "DateTime": datetime(2022, 2, 15),
    "Picture": "barbara.png"
}


comment2 = {
    "CommentId": 2,
    "Text": "Great location!",
    "Name": "Elena Kurkova",
    "Likes": ["Barbara Middleton"],
    "Comments": [],
    "DateTime": datetime(2022, 3, 24),
    "Picture": "elena.png"
}

test_comments = {
    1: comment1,
    2: comment2
}

location1 = {
    "LocationId": 1,
    "Name": "ABC Coffee Roasters",
    "Address": "Dmitrovka St, 17",
    "Comments": [comment1, comment2],
    "Picture": "restroom.png",
    "Stars": 4
}

test_location = {
    1: location1
}

user1 = {
    "UserId": 1,
    "Name": "Barbara Middleton",
    "Picture": "barbara.png",
    "Info": "I like exploring the city!",
    "Added": location1 
}

user2 = {
    "UserId": 2,
    "Name": "Elena Kurkova",
    "Picture": "elena.png",
    "Info": "I've been using the cup for 5 years."
}

test_users = {
    1: user1,
    2: user2
}

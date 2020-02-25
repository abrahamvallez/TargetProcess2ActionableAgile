# TargetProcess2ActionableAgile

# API Call: From Postman
****/api/history/v2/UserStory?where=(Team.id=54254) and (CurrentUserStory.CreateDate>DateTime.Parse("2019-07-01")) and (IsChangedEntityState=true)&take=2000&select={Date,CurrentUserStory:{CurrentUserStory.id,CurrentUserStory.name},EntityState:{EntityState.name}}&orderBy=CurrentUserStory,date&isodate=1

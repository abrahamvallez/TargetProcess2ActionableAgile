# TargetProcess2ActionableAgile

UserStories
****/api/history/v2/UserStory?take=2000&orderBy=CurrentUserStory,date&isodate=1&select={Date,CurrentUserStory:{CurrentUserStory.id,CurrentUserStory.name,CurrentUserStory.CycleTime,CurrentUserStory.customvalues},EntityState:{EntityState.name}, Feature}&where=(Team.id=54254) and (Project.id=113371) and (CurrentUserStory.CreateDate>DateTime.Parse("2020-02-01")) and (IsChangedEntityState=true)

Features

****/api/history/v2/Feature?take=2000&orderBy=CurrentFeature, date&isodate=1&select={Date,CurrentFeature:{CurrentFeature.id,CurrentFeature.name,CurrentFeature.CycleTime,CurrentFeature.customvalues},EntityState:{EntityState.name}}&where=(Team.id=11111) and (Project.id=111111) and (CurrentFeature.CreateDate>DateTime.Parse("2020-01-01")) and (IsChangedEntityState=true)

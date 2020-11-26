library(ggplot2)

dada = read.csv("mydata.csv", header = TRUE)

likes = unlist(dada["Likes"])


usrs = unlist(dada["Username"])

num_foll = unlist(dada["Followers"])


g <- ggplot(dada, aes(reorder(usrs, +num_foll), Likes))
g + geom_bar(stat = "identity") + labs(title = "likes-users",x = "USERNAMES", y = "LIKES")

g <- ggplot(dada, aes(reorder(usrs, +num_foll), num_foll))
g + geom_bar(stat = "identity") + labs(title = "Followers-users",x = "USERNAMES", y = "FOLLOWERS")
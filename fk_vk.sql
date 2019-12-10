USE vk;

DESC profiles;

ALTER TABLE profiles
  ADD CONSTRAINT profiles_user_id_fk 
    FOREIGN KEY (user_id) REFERENCES users(id)
      ON DELETE CASCADE,
  ADD CONSTRAINT profiles_photo_id_fk
    FOREIGN KEY (photo_id) REFERENCES media(id)
      ON DELETE SET NULL;
     
     
     
 DESC messages;

ALTER TABLE messages
  ADD CONSTRAINT messages_from_user_id_fk 
    FOREIGN KEY (from_user_id) REFERENCES users(id),
  ADD CONSTRAINT messages_to_user_id_fk 
    FOREIGN KEY (to_user_id) REFERENCES users(id);
   
   
 DESC communities;

ALTER TABLE communities
	ADD CONSTRAINT communities_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id);
 
 DESC communities_users;

ALTER TABLE communities_users
	ADD CONSTRAINT communities_users_community_id_fk
		FOREIGN KEY (community_id) REFERENCES communities(id),
	ADD CONSTRAINT user_id_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id);
			

 DESC friendship;

 ALTER TABLE friendship
	ADD CONSTRAINT user_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id),
	ADD CONSTRAINT friend_id_user_id_fk
		FOREIGN KEY (friend_id) REFERENCES users(id),
	ADD CONSTRAINT status_id_friendship_statuses_fk
		FOREIGN KEY (status_id) REFERENCES friendship_statuses(id);

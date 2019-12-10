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
	
DESC likes;


ALTER TABLE likes
	ADD CONSTRAINT user_like_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id),
	ADD CONSTRAINT target_id_media_id_fk
		FOREIGN KEY (target_id) REFERENCES media(id),
	ADD CONSTRAINT target_type_id_target_type_id_fk
		FOREIGN KEY (target_type_id) REFERENCES target_types(id),
	ADD CONSTRAINT like_type_id_like_types_id_fk
		FOREIGN KEY (like_type_id) REFERENCES like_types(id);

DESC posts;

ALTER TABLE posts
	ADD CONSTRAINT post_user_id_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id);
	
DESC media;

ALTER TABLE media
	ADD CONSTRAINT media_media_type_id_media_types_id_fk
		FOREIGN KEY (media_type_id) REFERENCES media_types(id),
	ADD CONSTRAINT media_user_id_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id);
	
	
	
DESC photo;

ALTER TABLE photo
	ADD CONSTRAINT photo_media_type_id_media_type_id_fk
		FOREIGN KEY (media_type_id) REFERENCES media_types(id),
	ADD CONSTRAINT photo_user_id_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id);
	

DESC relations;

ALTER TABLE relations
	ADD CONSTRAINT relations_user_id_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id),
	ADD CONSTRAINT relative_id_user_id_fk
		FOREIGN KEY (relative_id) REFERENCES users(id),
	ADD CONSTRAINT relations_status_id_relation_statuses_fk
		FOREIGN KEY (relation_status_id) REFERENCES relation_statuses(id);
	



package com.marek.loginnregistration.repositories;

import java.util.Optional;

import org.springframework.data.repository.CrudRepository;

import com.marek.loginnregistration.models.User;

public interface UserRepo extends CrudRepository<User, Long> {
	Optional<User> findByEmail(String email);	
	
}

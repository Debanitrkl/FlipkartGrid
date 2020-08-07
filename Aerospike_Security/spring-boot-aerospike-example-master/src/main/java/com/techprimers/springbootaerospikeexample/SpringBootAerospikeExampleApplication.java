package com.techprimers.springbootaerospikeexample;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

@SpringBootApplication
@EnableScheduling
public class SpringBootAerospikeExampleApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringBootAerospikeExampleApplication.class, args);
		
	}
}

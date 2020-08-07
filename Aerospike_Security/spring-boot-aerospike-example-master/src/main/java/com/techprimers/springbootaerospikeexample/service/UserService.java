package com.techprimers.springbootaerospikeexample.service;

import com.aerospike.client.AerospikeClient;
import com.aerospike.client.Key;
import com.aerospike.client.query.Statement;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class UserService {
    @Autowired
    AerospikeClient aerospikeClient;
    public void deleteExpiredTargetedCards(String Id) {
        if(Id == null || "".equals(Id)){
            Statement stmt = new Statement();
            stmt.setNamespace("test");
            stmt.setSetName("demo");
            aerospikeClient.execute(null, stmt, "script", "clean_record");
        }
        else{
            Key key = new Key("test","demo",Id);
            aerospikeClient.execute(null, key, "script", "clean_record");
        }

    }
}

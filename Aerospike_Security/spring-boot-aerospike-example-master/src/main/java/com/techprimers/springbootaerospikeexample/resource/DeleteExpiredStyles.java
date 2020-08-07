package com.techprimers.springbootaerospikeexample.resource;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.techprimers.springbootaerospikeexample.service.UserService;

@Component
@RestController
public class DeleteExpiredStyles {

	private static final Logger LOGGER = LoggerFactory.getLogger(DeleteExpiredStyles.class);

    @Autowired
    private UserService userService;

	// 6 pm on the last day of every month
	@Scheduled(cron = "0 0 18 L * ?")
	public void deleteExpiredCards() {
		try {
			userService.deleteExpiredTargetedCards(null);
			LOGGER.error("Job Executed Successfully");
		}
		catch(Exception e) {
			LOGGER.error("Error while deleting expired cards");
		}
	}

    @RequestMapping(value = "/debug/delete-by-id/",method = RequestMethod.DELETE)
    public void deleteById(@RequestParam(value = "Id") String Id){
        try{
            userService.deleteExpiredTargetedCards(Id);
        }
        catch(Exception e){
            LOGGER.error("Error while deleting targetedCardInfo by Id {}", e);
        }

    }

}

class Solution {
    public int solution(String phone_number) {
        if (phone_number.matches("010-\\d{4}-\\11d{4}")) {
            return 1;
        }
        else if(phone_number.matches("010\\d{8}")) {
            return 2;
        }
        else if (phone_number.matches("\\+82-10-\\d{4}-\\d{4}")) {
            return 3;
        }    
        else {
            return -1;
        }
    }
}
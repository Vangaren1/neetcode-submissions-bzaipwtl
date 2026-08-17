class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int fives(0), tens(0);

        for (auto bill : bills)
        {
            switch (bill)
            {
            case 5:
                fives++;
                break;
            case 10:
                if (fives == 0)
                {
                    return false;
                }
                fives--;
                tens++;
                break;
            case 20:
                if (fives == 0)
                {
                    return false;
                }
                if (tens == 0)
                {
                    if (fives < 3)
                    {
                        return false;
                    }
                    fives -= 3;
                    break;
                }
                if (fives == 0)
                {
                    return false;
                }
                tens--;
                fives--;
                break;
            }
        }
        return true;
    }
};
library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.STD_LOGIC_ARITH.all;

entity _8bit_BCD is
	port (
		CLK : in std_logic;
        	RST : in std_logic;
		DATA : in STD_LOGIC_VECTOR (7 downto 0);
		BCD_SIGN : out STD_LOGIC;
		BCD_DIGIT_1 : out STD_LOGIC_VECTOR (3 downto 0);
		BCD_DIGIT_2 : out STD_LOGIC_VECTOR (3 downto 0);
		BCD_DIGIT_3 : out STD_LOGIC_VECTOR (3 downto 0)
	);				  
end _8bit_BCD;

architecture Behavioral of _8bit_BCD is
signal INT_DATA_1 : INTEGER := 0;
signal INT_DATA_2 : INTEGER := 0;
signal INT_DATA_3 : INTEGER := 0;
signal SIGN : BIT := 0;
begin
	process(CLK, RST) begin
		if (RST='0') then
			INT_DATA_1 <= 0;
			INT_DATA_2 <= 0;
			INT_DATA_3 <= 0;
			sign <= 0;			
		elsif (CLK'event and CLK='1') then
			if (DATA[7]='1') then
				for i in 0 to 6 loop
					DATA[i] <= not DATA[i]
				end loop
				INT_DATA_1 <= conv_INTEGER(unsigned(DATA[0:6])) mod 100 / 10;
				INT_DATA_2 <= conv_INTEGER(unsigned(DATA[0:6])) mod 10 / 10;
				INT_DATA_3 <= conv_INTEGER(unsigned(DATA[0:6]))/ 10);
			end if;
			BCD_DIGIT_1 <= conv_std_logic_vector(INT_DATA_1, 4);
			BCD_DIGIT_2 <= conv_std_logic_vector(INT_DATA_2, 4);
			BCD_DIGIT_3 <= conv_std_logic_vector(INT_DATA_3, 4);
			BCD_SIGN <= SIGN
		end if;
	end process;
end Behavioral;
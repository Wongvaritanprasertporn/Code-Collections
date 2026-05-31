library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity adjust is
	port ( 
		CLK : in STD_LOGIC;
		KEY0 : in STD_LOGIC;
		KEY1 : in STD_LOGIC;
		SW0 : in STD_LOGIC;
		SEG : out STD_LOGIC_VECTOR (6 downto 0)
	);
end adjust;

architecture Behavioral of adjust is
signal count : INTEGER range 0 to 9 := 0;
signal KEY0_pressed, KEY1_pressed : STD_LOGIC := '0';
begin
	process (CLK, SW0) begin
		if SW0 = '0' then
			count <= 0;
		elsif rising_edge(clk) then
			if KEY0 = '1' and KEY0_pressed = '0' then
				if count = 9 then
					count <= 0;
				else
					count <= count + 1;
				end if;
			end if;
			if KEY1 = '1' and KEY1_pressed = '0' then
				if count = 0 then
					count <= 9;
				else
					count <= count - 1;
				end if;
			end if;
		end if;
		KEY0_pressed <= KEY0;
		KEY1_pressed <= KEY1;
	end process;

	process (count) begin
		case count is
			when 0 => SEG <= "1000000"; -- Display 0
			when 1 => SEG <= "1111001"; -- Display 1
			when 2 => SEG <= "0100100"; -- Display 2
			when 3 => SEG <= "0110000"; -- Display 3
			when 4 => SEG <= "0011001"; -- Display 4
			when 5 => SEG <= "0010010"; -- Display 5
			when 6 => SEG <= "0000010"; -- Display 6
			when 7 => SEG <= "1111000"; -- Display 7
			when 8 => SEG <= "0000000"; -- Display 8
			when 9 => SEG <= "0010000"; -- Display 9
			when others => SEG <= "1111111"; -- Blank (default)
		end case;
	end process;
end Behavioral;

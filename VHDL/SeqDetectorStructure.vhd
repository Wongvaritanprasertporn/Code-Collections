library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;  -- Preferred for arithmetic and logic operations

entity sequence_detector is port (
    clk     : in STD_LOGIC;
    rst     : in STD_LOGIC;
    seq_in  : in STD_LOGIC;
    seq_out : out STD_LOGIC
); end sequence_detector;

architecture Behavioral of sequence_detector is
type state_type is (S0, S1, S2, S3, S4);  -- Define the state type
signal state, next_state : state_type := S0;  -- Initialize state to S0
begin
    process(clk, rst)  -- Process to handle state transitions and outputs
    begin
        if rst = '1' then
            state <= S0;  -- Reset state to initial state
        elsif rising_edge(clk) then
            state <= next_state;  -- Move to the next state on clock edge
        end if;
    end process;

    process(state, seq_in)  -- Next state logic
    begin
        next_state <= state;  -- Default to remain in the same state (prevents latches)
        case state is
            when S0 =>
                if seq_in = '0' then
                    next_state <= S1;
                else
                    next_state <= S0;
                end if;
            when S1 =>
                if seq_in = '1' then
                    next_state <= S2;
                else
                    next_state <= S1;
                end if;
            when S2 =>
                if seq_in = '1' then
                    next_state <= S3;
                else
                    next_state <= S1;
                end if;
            when S3 =>
                if seq_in = '1' then
                    next_state <= S4;
                else
                    next_state <= S1;
                end if;
            when S4 =>
                next_state <= S0;  -- After detecting the sequence, return to S0
            when others =>
                next_state <= S0;
        end case;
    end process;
    seq_out <= '1' when state = S4 else '0';  -- Output logic: The sequence is detected in state S4
end Behavioral;

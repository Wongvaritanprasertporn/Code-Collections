library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity SeqDetectorLogic is port (
    clk     : in  STD_LOGIC;
    rst     : in  STD_LOGIC;
    seq_in  : in  STD_LOGIC;
    seq_out : out STD_LOGIC
); end SeqDetectorLogic;

architecture Behavioral of SeqDetectorLogic is
signal Q2, Q1, Q0 : STD_LOGIC;  -- State flip-flops (Q2, Q1, Q0) to hold the current state
signal D2, D1, D0 : STD_LOGIC;  -- Next-state signals
begin  -- State transition logic (next state generation)
    D2 <= (Q1 AND Q0 AND seq_in);  -- D flip-flop for Q2 (most significant bit of state)
    D1 <= (NOT Q2 AND Q0 AND seq_in) OR (Q2 AND NOT seq_in);  -- D flip-flop for Q1
    D0 <= (NOT Q2 AND NOT Q1 AND NOT Q0 AND NOT seq_in) OR  -- D flip-flop for Q0 (least significant bit of state)
          (NOT Q2 AND Q1 AND NOT Q0 AND NOT seq_in) OR
          (NOT Q2 AND NOT Q1 AND seq_in);
    seq_out <= Q2 AND NOT Q1 AND NOT Q0;  -- Output logic (sequence detected when in state S4)
    process(clk, rst) begin  -- State flip-flops with clock and reset
        if rst = '1' then  -- Asynchronous reset to set the state to S0 (000)
            Q2 <= '0';
            Q1 <= '0';
            Q0 <= '0';
        elsif rising_edge(clk) then  -- Update the state with the next-state values
            Q2 <= D2;
            Q1 <= D1;
            Q0 <= D0;
        end if;
    end process;
end Behavioral;

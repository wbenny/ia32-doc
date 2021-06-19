from utils.bit_field import BitField

class Cr0(BitField):
    """"""
    def __init__(self, value):
        super().__init__(value, size_in_bytes=8)

    _FIELDS = ["PE","MP","EM","TS","ET","NE","WP","AM","NW","CD","PG",]

    
    @property
    def PE(self):
        """
        Protection Enable
        Enables protected mode when set; enables real-address mode when
clear. This flag does not enable paging directly. It only enables segment-level protection. To enable paging,
both the PE and PG flags must be set.
        """
        return self[0:1]

    @PE.setter
    def PE(self, value):
        self[0:1] = value
    
    @property
    def MP(self):
        """
        Monitor Coprocessor
        Controls the interaction of the WAIT (or FWAIT) instruction with
the TS flag (bit 3 of CR0). If the MP flag is set, a WAIT instruction generates a device-not-available exception
(\#NM) if the TS flag is also set. If the MP flag is clear, the WAIT instruction ignores the setting of the TS flag.
        """
        return self[1:2]

    @MP.setter
    def MP(self, value):
        self[1:2] = value
    
    @property
    def EM(self):
        """
        FPU Emulation
        Indicates that the processor does not have an internal or external x87 FPU
when set; indicates an x87 FPU is present when clear. This flag also affects the execution of
MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instructions.

When the EM flag is set, execution of an x87 FPU instruction generates a device-not-available exception
(\#NM). This flag must be set when the processor does not have an internal x87 FPU or is not connected to
an external math coprocessor. Setting this flag forces all floating-point instructions to be handled by software
emulation.

Also, when the EM flag is set, execution of an MMX instruction causes an invalid-opcode exception (\#UD)
to be generated. Thus, if an IA-32 or Intel 64 processor incorporates MMX technology, the
EM flag must be set to 0 to enable execution of MMX instructions.
Similarly for SSE/SSE2/SSE3/SSSE3/SSE4 extensions, when the EM flag is set, execution of most
SSE/SSE2/SSE3/SSSE3/SSE4 instructions causes an invalid opcode exception (\#UD) to be generated.
If an IA-32 or Intel 64 processor incorporates the SSE/SSE2/SSE3/SSSE3/SSE4 extensions,
the EM flag must be set to 0 to enable execution of these extensions. SSE/SSE2/SSE3/SSSE3/SSE4
instructions not affected by the EM flag include: PAUSE, PREFETCHh, SFENCE, LFENCE, MFENCE, MOVNTI,
CLFLUSH, CRC32, and POPCNT.
        """
        return self[2:3]

    @EM.setter
    def EM(self, value):
        self[2:3] = value
    
    @property
    def TS(self):
        """
        Task Switched
        Allows the saving of the x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4
context on a task switch to be delayed until an x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instruction is
actually executed by the new task. The processor sets this flag on every task switch and tests it when
executing x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instructions.

- If the TS flag is set and the EM flag (bit 2 of CR0) is clear, a device-not-available exception (\#NM) is
  raised prior to the execution of any x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instruction; with the
  exception of PAUSE, PREFETCHh, SFENCE, LFENCE, MFENCE, MOVNTI, CLFLUSH, CRC32, and POPCNT.

- If the TS flag is set and the MP flag (bit 1 of CR0) and EM flag are clear, an \#NM exception is not raised
  prior to the execution of an x87 FPU WAIT/FWAIT instruction.

- If the EM flag is set, the setting of the TS flag has no effect on the execution of x87
  FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instructions.

  The processor does not automatically save the context of the x87 FPU, XMM, and MXCSR registers on a
  task switch. Instead, it sets the TS flag, which causes the processor to raise an \#NM exception whenever
  it encounters an x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instruction in the instruction stream for the
  new task (with the exception of the instructions listed above).

  The fault handler for the \#NM exception can then be used to clear the TS flag (with the CLTS instruction)
  and save the context of the x87 FPU, XMM, and MXCSR registers. If the task never encounters an x87
  FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4 instruction, the x87 FPU/MMX/SSE/SSE2/SSE3/SSSE3/SSE4
  context is never saved.
        """
        return self[3:4]

    @TS.setter
    def TS(self, value):
        self[3:4] = value
    
    @property
    def ET(self):
        """
        Extension Type
        Reserved in the Pentium 4, Intel Xeon, P6 family, and Pentium processors.
In the Pentium 4, Intel Xeon, and P6 family processors, this flag is hardcoded to 1. In the Intel386
and Intel486 processors, this flag indicates support of Intel 387 DX math coprocessor instructions when
set.
        """
        return self[4:5]

    @ET.setter
    def ET(self, value):
        self[4:5] = value
    
    @property
    def NE(self):
        """
        Numeric Error
        Enables the native (internal) mechanism for reporting x87 FPU errors
when set; enables the PC-style x87 FPU error reporting mechanism when clear. When the NE flag is clear
and the IGNNE\# input is asserted, x87 FPU errors are ignored. When the NE flag is clear and the IGNNE\#
input is deasserted, an unmasked x87 FPU error causes the processor to assert the FERR\# pin to generate
an external interrupt and to stop instruction execution immediately before executing the next waiting
floating-point instruction or WAIT/FWAIT instruction.

The FERR\# pin is intended to drive an input to an external interrupt controller (the FERR\# pin emulates the
ERROR\# pin of the Intel 287 and Intel 387 DX math coprocessors). The NE flag, IGNNE\# pin, and FERR\#
pin are used with external logic to implement PC-style error reporting. Using FERR\# and IGNNE\# to handle
floating-point exceptions is deprecated by modern operating systems; this non-native approach also limits
newer processors to operate with one logical processor active.
        """
        return self[5:6]

    @NE.setter
    def NE(self, value):
        self[5:6] = value
    
    @property
    def WP(self):
        """
        Write Protect
        When set, inhibits supervisor-level procedures from writing into readonly
pages; when clear, allows supervisor-level procedures to write into read-only pages (regardless of the
U/S bit setting). This flag facilitates implementation of the copy-onwrite
method of creating a new process (forking) used by operating systems such as UNIX.
        """
        return self[16:17]

    @WP.setter
    def WP(self, value):
        self[16:17] = value
    
    @property
    def AM(self):
        """
        Alignment Mask
        Enables automatic alignment checking when set; disables alignment
checking when clear. Alignment checking is performed only when the AM flag is set, the AC flag in the
EFLAGS register is set, CPL is 3, and the processor is operating in either protected or virtual-8086 mode.
        """
        return self[18:19]

    @AM.setter
    def AM(self, value):
        self[18:19] = value
    
    @property
    def NW(self):
        """
        Not Write-through
        When the NW and CD flags are clear, write-back (for Pentium 4,
Intel Xeon, P6 family, and Pentium processors) or write-through (for Intel486 processors) is enabled for
writes that hit the cache and invalidation cycles are enabled.
        """
        return self[29:30]

    @NW.setter
    def NW(self, value):
        self[29:30] = value
    
    @property
    def CD(self):
        """
        Cache Disable
        When the CD and NW flags are clear, caching of memory locations for
the whole of physical memory in the processors internal (and external) caches is enabled. When the CD
flag is set, caching is restricted. To prevent the processor from accessing and
updating its caches, the CD flag must be set and the caches must be invalidated so that no cache hits can
occur.
        """
        return self[30:31]

    @CD.setter
    def CD(self, value):
        self[30:31] = value
    
    @property
    def PG(self):
        """
        Paging Enable
        Enables paging when set; disables paging when clear. When paging is
disabled, all linear addresses are treated as physical addresses. The PG flag has no effect if the PE flag (bit
0 of register CR0) is not also set; setting the PG flag when the PE flag is clear causes a general-protection
exception (\#GP).

On Intel 64 processors, enabling and disabling IA-32e mode operation also requires modifying CR0.PG.
        """
        return self[31:32]

    @PG.setter
    def PG(self, value):
        self[31:32] = value
    
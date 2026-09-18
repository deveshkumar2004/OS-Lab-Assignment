import os

# Global constant for file operations demo
DATA_FILE = "practical4_sample.txt"

# SECTION 1: Process Creation & Management
def process_creation_demo():
    """
    Demonstrates process creation using fork(), replacing execution context
    using exec(), and process synchronization using wait().
    """
    pid = os.fork()
    
    if pid == 0:
        # Child process execution
        print(f"[CHILD] Running child process -> PID: {os.getpid()}, Parent PID: {os.getppid()}")
        # Replace child process image with echo command
        os.execlp("echo", "echo", "Status: Exec call successful inside the child process.")
    else:
        # Parent process waits for the child to terminate
        os.wait()
        print(f"[PARENT] Resumed parent process -> PID: {os.getpid()}, Parent PID: {os.getppid()}")

# SECTION 2: Low-Level File Descriptor Operations
def file_operations_demo():
    """
    Demonstrates direct system calls (open, write, read, close, remove)
    using file descriptors instead of high-level language wrappers.
    """
    # Open/create file for writing with truncation
    fd = os.open(DATA_FILE, os.O_CREAT | os.O_WRONLY | os.O_TRUNC)
    os.write(fd, b"Testing low-level system call I/O operations.\n")
    os.close(fd)

    # Reopen for read-only access
    fd = os.open(DATA_FILE, os.O_RDONLY)
    data = os.read(fd, 100)
    os.close(fd)

    print(f"I/O Complete for '{DATA_FILE}': {data.decode().strip()}")
    
    # Remove file from disk
    os.remove(DATA_FILE)

# SECTION 3: Device Node & Virtual File System Access
def device_interface_demo():
    """
    Demonstrates interacting with special device nodes (/dev/null)
    and reading virtual kernel system information (/proc/version).
    """
    # Discard data to /dev/null
    fd = os.open("/dev/null", os.O_WRONLY)
    os.write(fd, b"Redirecting unneeded stream to null.")
    os.close(fd)
    print("Direct write to /dev/null confirmed (stream discarded).")

    # Read virtual kernel details from /proc
    with open("/proc/version", "r") as f:
        print("Kernel Build Info (/proc/version):", f.readline().strip())

# SECTION 4: System-Level Error Handling
def error_handling_demo():
    """
    Demonstrates handling low-level OS errors gracefully using OSError.
    """
    try:
        os.open("/non_existent_directory/dummy_file.txt", os.O_RDONLY)
    except OSError as e:
        print(f"System error captured as expected: {e}")

# MAIN EXECUTION PIPELINE
if __name__ == "__main__":
    print("=== PART 1: PROCESS CREATION (fork + exec) ===")
    process_creation_demo()

    print("\n=== PART 2: LOW-LEVEL FILE OPERATIONS ===")
    file_operations_demo()

    print("\n=== PART 3: DEVICE NODE & VFS ACCESS ===")
    device_interface_demo()

    print("\n=== PART 4: OS-LEVEL ERROR HANDLING ===")
    error_handling_demo()

    print("\n=== EXECUTION SUMMARY ===")
    print("- Process management (fork, wait, exec): Completed")
    print("- File operations (open, write, read, close, unlink): Completed")
    print("- Device node (/dev/null) and procfs access: Completed")
    print("- Low-level exception recovery: Completed")
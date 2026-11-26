import gc
import time
import tracemalloc

# Function to create cyclic objects
def create_cycles(number):
    for _ in range(number):
        list1 = []
        list2 = []

# Create a circular reference
    list1.append(list2)
    list2.append(list1)

# Display garbage collector information
print("Automatic GC enabled:", gc.isenabled())
print("Initial GC counters:", gc.get_count())

# Start tracking memory usage
tracemalloc.start()

# Remove any previously collected garbage
gc.collect()

# Record memory before creating objects
before_memory = tracemalloc.get_traced_memory()[0]

# Create many cyclic objects
start_time = time.perf_counter()
create_cycles(100000)
creation_time = time.perf_counter() - start_time

# Measure memory before manual collection
memory_before_gc = tracemalloc.get_traced_memory()[0]

print("\n--- Before Manual Garbage Collection ---")
print("Memory before creation:", before_memory, "bytes")
print("Memory after creation:", memory_before_gc, "bytes")
print("Object creation time:", round(creation_time, 4), "seconds")

# Manually trigger garbage collection
start_time = time.perf_counter()
collected_objects = gc.collect()
collection_time = time.perf_counter() - start_time

# Measure memory after collection

memory_after_gc = tracemalloc.get_traced_memory()[0]

print("\n--- After Manual Garbage Collection ---")
print("Collected unreachable objects:", collected_objects)
print("Memory after collection:", memory_after_gc, "bytes")
print("Garbage collection time:",
round(collection_time, 4), "seconds")

# Calculate memory reduction
memory_reduced = memory_before_gc - memory_after_gc

print("\n--- Performance Analysis ---")
print("Memory reduction:", memory_reduced, "bytes")
print("GC statistics:", gc.get_stats())
print("Final GC counters:", gc.get_count())

# Stop memory tracking
tracemalloc.stop()

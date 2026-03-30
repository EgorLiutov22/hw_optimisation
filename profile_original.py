import cProfile
import pstats
import io
from original_main import main


def profile_code():
    profiler = cProfile.Profile()
    profiler.enable()

    main()

    profiler.disable()


    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats(20)
    print(s.getvalue())


if __name__ == "__main__":
    profile_code()
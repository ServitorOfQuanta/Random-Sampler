import pytest
from sampler import sample

class TestSampler:
    @pytest.mark.parametrize('execution_number', range(10))
    def test_sampler_happy_path(self, execution_number):
        n = 5
        pool_m = range(10)

        samples = sample(pool_m, n)

        assert len(samples) == n
        assert len(set(samples)) == len(samples), "Values should be unique given pool"

    def test_sampler_negative_n(self):
        n = -1 
        pool_m = range(10)

        with pytest.raises(AssertionError):
            sample(pool_m, n)

    def test_sampler_n_larger_than_m(self):
        n = 11
        pool_m = range(10)

        with pytest.raises(AssertionError):
            sample(pool_m, n)

    def test_sampler_happy_path_n_0(self):
        n = 0
        pool_m = range(10)

        samples = sample(pool_m, n)

        assert len(samples) == n
        assert samples == []

    @pytest.mark.parametrize("pool", [1, {1: "a", 2: "b"}])
    def test_sampler_m_pool_not_sequence(self, pool):
        n = 1

        with pytest.raises(TypeError):
            sample(pool, n)

    @pytest.mark.parametrize("n", [1.5, 'a', "hello", range(10), {1: "a", 2: "b"}])
    def test_sampler_n_not_int(self, n):
        pool_m = range(10)

        with pytest.raises(TypeError):
            sample(pool_m, n)
    
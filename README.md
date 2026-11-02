# NumPy Tutorial for Beginners

A hands-on introduction to [NumPy](https://numpy.org/), the library that pretty much all numerical and data work in Python is built on. Each topic is a short Jupyter notebook with small examples you can run, change and break.

Everything has been updated for **NumPy 2.x**.

## Contents

| # | Notebook | What's in it |
|---|---|---|
| 0 | [Data Types](0.%20Data%20Types.ipynb) | dtypes, type codes, conversion, overflow, promotion, strings |
| 1 | [Create an Array](1.%20Create%20an%20Array.ipynb) | `array`, `arange`, `linspace`, `zeros`/`ones`/`full`, `eye`, `meshgrid` |
| 2 | [Inspect an Array](2.%20Inspect%20an%20Array.ipynb) | shape, size, memory use, strides |
| 3 | [Sampling Methods](3.%20Sampling%20Methods.ipynb) | the `Generator` API, distributions, `choice`, shuffling, legacy API |
| 4 | [Math Functions](4.%20Math%20Functions.ipynb) | what `axis` means, arithmetic, rounding, statistics, comparisons |
| 5 | [Slicing & Indexing](5.%20Slicing%20%26%20Indexing.ipynb) | slicing, boolean masks, fancy indexing, `where`, `select` |
| 6 | [Sort an Array](6.%20Sort%20an%20Array.ipynb) | `sort`, `argsort`, `lexsort`, `partition`, `searchsorted` |
| 7 | [Manipulate an Array](7.%20Manipulate%20an%20Array.ipynb) | reshape, transpose, flatten, adding/removing axes and elements |
| 8 | [Combine & Split an Array](8.%20Combine%20%26%20Split%20an%20Array.ipynb) | `concatenate`, `stack`, `block`, `split`, `array_split` |
| 9 | [Set Operations](9.%20Set%20Operations.ipynb) | `unique`, intersection/union/difference, `isin` |
| 10 | [Linear Algebra](10.%20Linear%20Algebra.ipynb) | `@`, norms, `solve`, `lstsq`, eigenvalues, QR, SVD |
| 11 | [Broadcasting](11.%20Broadcasting.ipynb) | the rules, practical uses, and common traps |
| 12 | [Views and Copies](12.%20Views%20and%20Copies.ipynb) | when changing one array changes another |
| 13 | [Vectorization & Ufuncs](13.%20Vectorization%20%26%20Ufuncs.ipynb) | why loops are slow and how to get rid of them |
| 14 | [Missing Values](14.%20Missing%20Values.ipynb) | NaN, inf, `nan*` functions, filling, masked arrays |
| 15 | [Saving & Loading Arrays](15.%20Saving%20%26%20Loading%20Arrays.ipynb) | `.npy`/`.npz`, memory mapping, CSV |
| 16 | [Exercises](16.%20Exercises.ipynb) | 17 practice problems with solutions |

If you'd rather read it all in one go, [Complete Tutorial.ipynb](Complete%20Tutorial.ipynb) has chapters 0 to 15 in a single notebook.

### Suggested order

If you're completely new to NumPy, go through 0 to 5 in order, then read **11 (Broadcasting)** and **12 (Views and Copies)** before the rest. Those two explain most of the confusing behaviour you'll run into later. After that, pick whatever you need.

## Running the notebooks

```bash
git clone https://github.com/eric496/numpy-tutorial.git
cd numpy-tutorial
pip install -r requirements.txt
jupyter lab
```

You can also open any notebook directly in [Google Colab](https://colab.research.google.com/) via *File → Open notebook → GitHub* and pasting the repo URL.

Most examples use a seeded random generator (`np.random.default_rng(seed)`), so you should see the same numbers as the saved outputs. The exception is the timing examples in notebook 13, which depend on your machine.

## Upgrading from older NumPy?

The notebooks used to target NumPy 1.x. If you're following along with older code, these are the changes you're most likely to hit:

- `np.string_` / `np.unicode_` are gone, use `np.bytes_` / `np.str_`
- `np.in1d` is gone, use `np.isin`
- `np.random.seed` + `np.random.rand` still work, but `np.random.default_rng()` is the recommended way
- Python scalars no longer upcast arrays (`float32_array + 1.0` stays `float32`)

The [NumPy 2.0 migration guide](https://numpy.org/doc/stable/numpy_2_0_migration_guide.html) has the full list.

## Contributing

Found a mistake or something that's unclear? Issues and pull requests are welcome.

If you edit a notebook, please re-run it top to bottom so the saved outputs match, and then regenerate the combined notebook:

```bash
python tools/build_complete.py
```

## Further reading

- [NumPy user guide](https://numpy.org/doc/stable/user/index.html)
- [NumPy: the absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [From Python to NumPy](https://www.labri.fr/perso/nrougier/from-python-to-numpy/) by Nicolas Rougier, a great next step once you're comfortable with the basics

## License

[MIT](LICENSE)

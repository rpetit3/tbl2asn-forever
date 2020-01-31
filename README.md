# tbl2asn-forever Conda
This fork is specifically meant for creating a `tbl2asn-forever` recipe for BioConda. To see the original repository please checkout https://github.com/audy/tbl2asn-forever

To make this work for Bioconda, binaries for version 25.7 of tbl2asn are included in this repository.

```
conda create -n tbl2asn-forever -c conda-forge -c bioconda tbl2asn-forever
```
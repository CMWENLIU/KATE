running records on KATE:

python construct_20news.py -train train/allnews/ -test test/allnews/ -o outdir
python train.py -i outdir/train.corpus  -nv 9000 --noise gs  -ctype kcomp -nd 2000 -sm model_2000
python pred.py -i bbcdata_prepare/train.corpus  -lm model_2000  -o output/training_2000.txt -e output/tr_embedding.txt
python pred.py -i bbcdata_prepare/test.corpus  -lm model_2000  -o output/test_2000.txt -e output/te_embedding.txt
python run_classifier.py output/training_2000.txt bbcdata_prepare/train.labels output/test_2000.txt bbcdata_prepare/test.labels -nv 200 -cv 10
----------------------------------------

python construct_20news.py -train train/allnews/ -test test/allnews/ -o outdir
python train.py -i outdir/train.corpus  -nv 9000 --noise gs  -ctype kcomp -nd 2000
python pred.py -i bbcdata_prepare/train.corpus  -lm model  -o output/training.txt -e output/tr_embedding.txt
python pred.py -i bbcdata_prepare/test.corpus  -lm model  -o output/test.txt -e output/te_embedding.txt
python run_classifier.py output/training.txt bbcdata_prepare/train.labels output/test.txt bbcdata_prepare/test.labels -nv 200 -cv 10

-----------------
python train.py -i outdir/train.corpus  -nv 500  -ctype kcomp
python pred.py -i outdir/test.corpus -lm model  -o output/a.txt
python run_classifier.py output/tr.txt outdir/train.labels output/te.txt outdir/test.labels -nv 300 -cv 10

running records on KATE:

python construct_20news.py -train mixmodel/mixdata/ -test test/allnews/ -o mixmodel/classf_test/
python construct_20news.py -train mixmodel/mixdata/ -test train/allnews/ -o mixmodel/classf_train/
python train.py -i mixmodel/classf_train/train.corpus  -nv 10000 --noise gs  -ctype kcomp -nd 2000 -sm mixmodel/model_2000
python pred.py -i mixmodel/classf_train/test.corpus  -lm mixmodel/model_2000  -o mixmodel/training_2000.txt -e mixmodel/tr_embedding.txt
python pred.py -i mixmodel/classf_test/test.corpus  -lm mixmodel/model_2000  -o mixmodel/test_2000.txt -e mixmodel/te_embedding.txt
python run_classifier.py mixmodel/training_2000.txt mixmodel/classf_train/test.labels mixmodel/test_2000.txt mixmodel/classf_test/test.labels -nv 2000 -cv 10
python run_classifier.py mixmodel/tr_embedding.txt  mixmodel/classf_train/test.labels mixmodel/te_embedding.txt  mixmodel/classf_test/test.labels -nv 2000 -cv 10
-------------------------------------------
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

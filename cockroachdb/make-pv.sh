rm -rf /cockroachdata
mkdir /cockroachdata
mkdir /cockroachdata/pv-0
mkdir /cockroachdata/pv-1
mkdir /cockroachdata/pv-2
kubectl apply -f pv.yaml

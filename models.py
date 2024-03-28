from django.db import models

class Asset(models.Model):
    asset_id = models.IntegerField(primary_key=True)
    ip_address = models.CharField(max_length=255)
    hostname = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    asset_type = models.CharField(max_length=255)
    last_scan_date = models.DateField()

class Scan(models.Model):
    scan_id = models.IntegerField(primary_key=True)
    scan_type = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    scanner_used = models.CharField(max_length=100)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

class ScanResult(models.Model):
    scan_result_id = models.IntegerField(primary_key=True)
    scan = models.ForeignKey(Scan, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    vulnerability_id = models.IntegerField()
    result_time = models.DateTimeField()

class Reporting(models.Model):
    report_id = models.IntegerField(primary_key=True)
    report_name = models.CharField(max_length=100)
    user_id = models.IntegerField()
    creation_time = models.DateTimeField()
    scan_result = models.ForeignKey(ScanResult, on_delete=models.CASCADE)

class Role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=255)

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class Vulnerability(models.Model):
    vulnerability_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    severity = models.CharField(max_length=50)
    cvss_score = models.DecimalField(max_digits=4, decimal_places=2)
    remediation = models.ForeignKey('RemediationRec', related_name='vulnerability_remediations', on_delete=models.CASCADE)

class RemediationRec(models.Model):
    remediation_rec_id = models.IntegerField(primary_key=True)
    action_description = models.TextField()
    status = models.CharField(max_length=255)
     

class Vulnerability(models.Model):
    title = models.CharField(max_length=100)
    severity = models.CharField(max_length=50)
    date_detected = models.DateTimeField()

    def __str__(self):
        return self.title

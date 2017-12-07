import os
import subprocess
import shutil
import filecmp
from filecmp import cmp
from os.path import join, exists

data_base_dir = 'pipeline_stages'
out_base_dir = 'output'

if os.path.exists(out_base_dir):
    shutil.rmtree(out_base_dir)

def run(*args, **kwargs):
    return subprocess.check_call(*args, **kwargs)

def bam_match(f1, f2):
    bam_diff_command = [
        'bam', 'diff',
        '--all',
        '--in1', f1,
        '--in2', f2
    ]
    
    output = subprocess.check_output(bam_diff_command)
    return len(output) == 0

def files_match(f1, f2):
    return filecmp.cmp(f1, f2, shallow=False)

def dirs_match(d1, d2):
    match, mismatch, errors = filecmp.cmpfiles(d1, d2, os.listdir(d1),
        shallow=False)

    return len(mismatch) == 0 and len(errors) == 0

def test_sisrs():
    run(['pip', 'freeze'])

#def test_align_contigs():
#
#    data_dir = join(data_base_dir, '0_RawData_PremadeGenome')
#    exp_base_dir = join(data_base_dir, '1_alignContigs')
#    contig_dirname = 'premadeoutput'
#    contig_dir = join(out_base_dir, contig_dirname)
#    taxon_names = [
#        'GorGor',
#        # TODO: figure out why HomSap isn't passing
#        #'HomSap',
#        'HylMol',
#        'MacFas',
#        'MacMul',
#        'PanPan',
#        'PanTro',
#        'PonPyg'
#    ]
#
#    command = [
#        'sisrs-python',
#        '-p', '8',
#        '-a', 'premade',
#        '-c', '0',
#        '-f', data_dir,
#        '-z', out_base_dir,
#        'align_contigs'
#    ]
#    run(command)
#
#    assert(dirs_match(
#        join(out_base_dir, 'premadeoutput'),
#        join(exp_base_dir, 'premadeoutput')))
#
#    for taxon_name in taxon_names:
#        out_dir = join(out_base_dir, taxon_name)
#        exp_dir = join(exp_base_dir, taxon_name)
#
#        out_bam_path = join(out_dir, taxon_name + '.bam')
#        exp_bam_path = join(exp_dir, taxon_name + '.bam')
#
#        assert(bam_match(out_bam_path, exp_bam_path))
        


#def test_output_alignment():
#
#    data_dir = join(data_base_dir, '2_identifyFixedSites')
#    exp_dir = join(data_base_dir, '3_outputAlignment')
#    out_dir = out_base_dir
#
#    command = [
#        'sisrs-python',
#        '-f', data_dir,
#        '-z', out_dir,
#        'output_alignment'
#    ]
#    run(command)
#
#    assert cmp(
#        join(out_dir, 'alignment.nex'),
#        join(exp_dir, 'alignment.nex'))

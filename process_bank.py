import pandas as pd
import numpy as np

def process_bank_df(df):
    signup = (df['y'] == 'yes')
    signup.name = 'sign_up'
    
    age = pd.get_dummies(pd.cut(df['age'], [0, 25, 30, 40, 50, 60, np.inf], right=False))
    age.columns = ['age_lt_25', 'age_25_to_30', 'age_30_to_40', 'age_40_to_50', 'age_50_to_60', 'age_ge_60']
    
    job = pd.get_dummies(df['job'])
    job = job[['unemployed','retired','student','housemaid','management','entrepreneur','blue-collar', 'technician', 'admin.', 'services']]
    job.columns = ['job_unemployed', 'job_retired', 'job_student', 'job_housemaid', 'job_management', 'job_entrepreneur', 'job_blue_collar', 'job_technician', 'job_admin', 'job_services']

    marital = pd.get_dummies(df['marital'])
    marital = marital[['married', 'single', 'divorced']]
    
    education = pd.get_dummies(df['education'])
    education = education[['university.degree', 'high.school', 'basic.4y', 'basic.6y', 'basic.9y', 'professional.course']]
    education.columns = ['education_university', 'education_highschool', 'education_basic4yr', 'education_basic6yr', 'education_basic9yr', 'education_professional']

    default = (df['default'] != 'no')
    default.name = 'credit_is_or_may_be_in_default'

    housing = (df['housing'] == 'yes')
    housing.name = 'has_housing_loan'

    loan = (df['loan'] == 'yes')
    loan.name = 'has_personal_loan'

    contact = pd.get_dummies(df['contact'])
    contact = contact[['cellular','telephone']]
    contact.columns = ['called_cellphone', 'called_landline']

    q1 = (df['month'] == 'jan') | (df['month'] == 'feb') | (df['month'] == 'mar')
    q2 = (df['month'] == 'apr') | (df['month'] == 'may') | (df['month'] == 'jun')
    q3 = (df['month'] == 'jul') | (df['month'] == 'aug') | (df['month'] == 'sep')
    q4 = (df['month'] == 'oct') | (df['month'] == 'nov') | (df['month'] == 'dec')
    q1.name = 'call_in_Q1'
    q2.name = 'call_in_Q2'
    q3.name = 'call_in_Q3'
    q4.name = 'call_in_Q4'

    dayofweek = pd.get_dummies(df['day_of_week'])
    dayofweek = dayofweek[['mon', 'tue', 'wed', 'thu', 'fri']]
    dayofweek.columns = ['call_on_mon', 'call_on_tue', 'call_on_wed', 'call_on_thu', 'call_on_fri']

    anyprior = (df['campaign'] > 1)
    anyprior.name = 'any_prior_calls_in_campaign'
    
    multprior = (df['campaign'] > 2)
    multprior.name = 'mult_prior_calls_in_campaign'

    calledbefore = (df['pdays'] < 999)
    calledbefore.name = 'called_before'

    anypriorbefore = (df['previous'] > 0)
    anypriorbefore.name = 'any_prior_calls_b4_campaign'
    multpriorbefore = (df['previous'] > 1)
    multpriorbefore.name = 'mult_prior_calls_b4_campaign'

    priorcampaign = pd.get_dummies(df['poutcome'])
    priorcampaign = priorcampaign[['failure','success']]
    priorcampaign.columns = ['calls_b4_campaign_failed', 'calls_b4_campaign_successful']

    emp_var_rate_lt_n1 = (df['emp.var.rate'] < -1)
    emp_var_rate_lt_n1.name = 'emp_var_rate_lt_n1'
    emp_var_rate_gt_1 = (df['emp.var.rate'] > 1)
    emp_var_rate_gt_1.name = 'emp_var_rate_gt_1'

    nr_employed_lt_5100 = (df['nr.employed'] < 5100)
    nr_employed_lt_5100.name = 'nr_employed_lt_5100'
    nr_employed_gt_5100 = (df['nr.employed'] > 5100)
    nr_employed_gt_5100.name = 'nr_employed_gt_5100'

    cons_price_idx_geq_93_5 = (df['cons.price.idx'] >= 93.5)
    cons_price_idx_geq_93_5.name = 'cons_price_idx_geq_93_5'
    
    cons_conf_idx_leq_n40 = (df['cons.conf.idx'] <= -40)
    cons_conf_idx_leq_n40.name = 'cons_conf_idx_leq_n40'
    
    euribor3m_geq_100 = (df['euribor3m'] >= 1)
    euribor3m_geq_100.name = 'euribor3m_geq_100'
    euribor3m_geq_200 = (df['euribor3m'] >= 2)
    euribor3m_geq_200.name = 'euribor3m_geq_200'
    euribor3m_geq_300 = (df['euribor3m'] >= 3)
    euribor3m_geq_300.name = 'euribor3m_geq_300'
    euribor3m_geq_400 = (df['euribor3m'] >= 4)
    euribor3m_geq_400.name = 'euribor3m_geq_400'
    euribor3m_geq_500 = (df['euribor3m'] >= 5)
    euribor3m_geq_500.name = 'euribor3m_geq_500'
    
    return pd.concat([signup, age, job, marital, education, default, housing, loan, contact,
                      q1, q2, q3, q4, dayofweek, anyprior, multprior, calledbefore, anypriorbefore,
                     multpriorbefore, priorcampaign, emp_var_rate_lt_n1, emp_var_rate_gt_1,
                     nr_employed_lt_5100, nr_employed_gt_5100, cons_price_idx_geq_93_5,
                      cons_conf_idx_leq_n40, euribor3m_geq_100, euribor3m_geq_200, euribor3m_geq_300,
                     euribor3m_geq_400, euribor3m_geq_500], axis=1)

if __name__ == '__main__':
    df = pd.read_csv('data/bank-additional-full.csv', sep=';')
    df = process_bank_df(df)
    df.to_csv('data/bank_data.csv', index=False)